from Domain.Repository.RecipeRepositoryInterface import RecipeRepositoryInterface
from Application.DTO.RecipeDTOs import RecipeListResponse

from uuid import UUID
from typing import List

class ListRecipesUseCase:
    def __init__(self, repository: RecipeRepositoryInterface) -> List[RecipeListResponse]:
        self.repository = repository

    def execute(self, owner_id: UUID):
        recipes = self.repository.find_by_owner(owner_id)

        return [
            RecipeListResponse(
                id=recipe.id,
                name=recipe.name,
                description=recipe.description
            ) for recipe in recipes
        ]
        