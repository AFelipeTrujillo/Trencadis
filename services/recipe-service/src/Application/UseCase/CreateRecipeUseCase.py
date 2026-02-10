from Domain.Repository.RecipeRepositoryInterface import RecipeRepositoryInterface
from Domain.Entity.Recipe import Recipe
from Domain.ValueObject.Ingredient import Ingredient
from Domain.ValueObject.MeasurementUnit import MeasurementUnit
from Application.DTO.RecipeDTOs import CreateRecepieRequest
from uuid import UUID

class CreateRecipeUseCase:
    """ Use case for creating a new recipe. """
    
    def __init__(self, repository: RecipeRepositoryInterface):
        self.repository = repository
    
    async def execute(self, owner_id: UUID, request: CreateRecepieRequest) -> Recipe:
        
        ingredients = []
        # Convert ingredients_data to Ingredient objects
        for ingredient_data in request.ingredients:
            ingredient = Ingredient(
                name=ingredient_data.name,
                amount=ingredient_data.amount,
                unit=MeasurementUnit(ingredient_data.unit)
            )
            ingredients.append(ingredient)
        
        # Create the Recipe entity
        recipe = Recipe(
            name=request.name,
            description=request.description,
            owner_id=owner_id,
            ingredients=ingredients
        )

        await self.repository.save(recipe)
        return recipe