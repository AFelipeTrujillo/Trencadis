from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase

from Infrastructure.Config.Settings import Settings

DATABASE_URL = Settings().DATABASE_URL

# Asynchronous engine and session setup
# echo=True is set to True for SQL query logging; set to False in production
# future=True enables 2.0 style usage
engine = create_async_engine(DATABASE_URL, echo=True, future=True)

# Create a configured "AsyncSession" class
# expire_on_commit=False will prevent attributes from being expired
# after commit so that they can be accessed without reloading from the database
# autoCommit and autoFlush are set to False to give more control over transactions
AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
    autoCommit=False,
    autoFlush=False
)

class Base(DeclarativeBase):
    pass

async def get_db():
    async with AsyncSessionLocal() as session:
        try:
            yield session
            await session.commit()
        except:
            await session.rollback()
            raise
        finally:
            await session.close()