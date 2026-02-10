import asyncio
import pytest
import pytest_asyncio
from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from sqlalchemy.pool import NullPool
from httpx import ASGITransport, AsyncClient

from Infrastructure.Persistence.Database import Base
from Infrastructure.Config.Settings import settings
from Infrastructure.Delivery.Http.FastAPI.main import app, auth_guard
from Infrastructure.Persistence.Database import get_db

# 1. FORZAR EL LOOP DE SESIÓN
# Esto asegura que todos los fixtures compartan el mismo corazón de ejecución
@pytest.fixture(scope="session")
def event_loop():
    policy = asyncio.get_event_loop_policy()
    loop = policy.new_event_loop()
    yield loop
    loop.close()

# 2. ENGINE (Scope Session)
@pytest_asyncio.fixture(scope="session")
async def engine():
    engine = create_async_engine(
        settings.TEST_DATABASE_URL,
        poolclass=NullPool,
        pool_pre_ping=True,
    )
    
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    
    yield engine
    
    # Teardown: Intentamos borrar tablas, si falla por el loop, el dispose lo arregla
    try:
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.drop_all)
    except Exception:
        pass
    finally:
        await engine.dispose()

# 3. DB_SESSION (Manual para evitar el error de 'shield')
@pytest_asyncio.fixture(scope="function")
async def db_session(engine) -> AsyncGenerator[AsyncSession, None]:
    async_session = async_sessionmaker(
        bind=engine,
        class_=AsyncSession,
        expire_on_commit=False,
        autocommit=False,
        autoflush=False
    )
    
    # Creamos la sesión manualmente
    session = async_session()
    try:
        yield session
    finally:
        # Cerramos manualmente capturando el posible RuntimeError del loop
        try:
            await session.close()
        except RuntimeError:
            # El loop ya se cerró, asyncpg no puede hacer nada, ignoramos
            pass

# 4. OVERRIDE_AUTH
@pytest_asyncio.fixture(scope="function")
async def override_auth(mock_user_id):
    async def _mock_auth():
        return {
            "sub": mock_user_id,
            "email": "test@trencadis.com",
            "preferred_username": "testuser"
        }
    app.dependency_overrides[auth_guard] = _mock_auth
    yield
    app.dependency_overrides.pop(auth_guard, None)

# 5. CLIENT (Inyectando la sesión correctamente)
@pytest_asyncio.fixture(scope="function")
async def client(db_session, override_auth) -> AsyncGenerator[AsyncClient, None]:
    # Inyectamos la dependencia de DB
    app.dependency_overrides[get_db] = lambda: db_session
    
    async with AsyncClient(
        transport=ASGITransport(app=app), 
        base_url="http://test"
    ) as ac:
        yield ac
    
    # Limpiamos todo al terminar el test
    app.dependency_overrides.clear()

@pytest.fixture
def mock_user_id():
    return "550e8400-e29b-41d4-a716-446655440000"