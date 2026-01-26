from fastapi import FastAPI, Depends
from fastapi.responses import JSONResponse
from fastapi import status
from uuid import UUID
from typing import List

from Domain.Exception.DomainException import DomainException

from Application.UseCase.CreateRecipeUseCase import CreateRecipeUseCase
from Application.UseCase.ListRecipesUseCase import ListRecipesUseCase
from Application.DTO.RecipeDTOs import CreateRecepieRequest, RecipeListResponse

from Infrastructure.Delivery.Http.Security.KeycloakGuard import KeycloakGuard
from Infrastructure.Persistence.InMemory.InMemoryRecipeRepository import InMemoryRecipeRepository

app = FastAPI(title="Trencadís Recipe Service", version="1.0.0")
auth_guard = KeycloakGuard()

recipe_repo = InMemoryRecipeRepository()
create_recipe_use_case = CreateRecipeUseCase(repository=recipe_repo)
list_recipes_use_case = ListRecipesUseCase(repository=recipe_repo)

@app.post("/recipes")
async def create_recipe(
        request: CreateRecepieRequest, 
        user_data=Depends(auth_guard)):
    
    owner_id = UUID(user_data.get("sub"))
    create_recipe_use_case.execute(owner_id=owner_id, request=request)
    return {
        "id": str(request.id),
        "name": request.name,
        "message": "Recipe created successfully"
    }

@app.get("/recipes", response_model=List[RecipeListResponse])
async def list_recipes(user_data: dict = Depends(auth_guard)):
    owner_id = UUID(user_data.get("sub"))
    recipes = list_recipes_use_case.execute(owner_id=owner_id)
    return recipes

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