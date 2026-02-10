from fastapi import FastAPI, Depends
from fastapi.responses import JSONResponse
from fastapi import status
from uuid import UUID
from typing import List

from sqlalchemy.ext.asyncio import AsyncSession

from Domain.Exception.DomainException import DomainException

from Application.DTO.RecipeDTOs import CreateRecepieRequest, RecipeListResponse
from Application.Factory.RecipeUseCaseFactoryInterface import RecipeUseCaseFactoryInterface

from Infrastructure.Delivery.Http.Security.KeycloakGuard import KeycloakGuard
from Infrastructure.Persistence.Database import get_db
from Infrastructure.Persistence.SQLAlchemy.Factories.RecipeUseCaseFactory import RecipeUseCaseFactory as SQLAlchemyRecipeUseCaseFactory

app = FastAPI(title="Trencadís Recipe Service", version="1.0.0")
auth_guard = KeycloakGuard()

@app.post("/recipes")
async def create_recipe(
        request: CreateRecepieRequest, 
        user_data=Depends(auth_guard),
        db = Depends(get_db)
):
    owner_id = UUID(user_data.get("sub"))
    factory: RecipeUseCaseFactoryInterface = SQLAlchemyRecipeUseCaseFactory(db)
    use_case = factory.create_create_recipe_use_case()
    recipie = await use_case.execute(owner_id, request=request)

    return {
        "id": str(recipie.id),
        "name": request.name,
        "message": "Recipe created successfully"
    }

@app.get("/recipes", response_model=List[RecipeListResponse])
async def list_recipes(
    user_data: dict = Depends(auth_guard),
    db: AsyncSession = Depends(get_db)
):
    factory: RecipeUseCaseFactoryInterface = SQLAlchemyRecipeUseCaseFactory(db)
    use_case = factory.create_list_recipes_use_case()
    recipies = await use_case.execute(owner_id=UUID(user_data.get("sub")))
    return recipies

@app.exception_handler(DomainException)
def domain_exception_handler(request, exc: DomainException):
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content={
            "error": "Domain Error",
            "type": exc.__class__.__name__,
            "message": str(exc)
        },
    )