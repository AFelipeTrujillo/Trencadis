from Domain.Repository.RecipeRepositoryInterface import RecipeRepositoryInterface
from Domain.Entity.Recipe import Recipe
from Domain.ValueObject.Ingredient import Ingredient
from Domain.ValueObject.MeasurementUnit import MeasurementUnit
from uuid import UUID

class CreateRecipeUseCase:

    def __init__(self, repository: RecipeRepositoryInterface):
        self.repository = repository
    
    def execute(self, wner_id: UUID, name: str, description: str, ingredients_data: list) -> Recipe:
        
        ingredients = []
        # Convert ingredients_data to Ingredient objects
        for ingredient_data in ingredients_data:
            ingredient = Ingredient(
                name=ingredient_data['name'],
                amount=ingredient_data['amount'],
                unit=MeasurementUnit(ingredient_data['unit'])
            )
            ingredients.append(ingredient)
        
        recipe = Recipe(
            name=name,
            description=description,
            owner_id=wner_id,
            ingredients=ingredients
        )

        self.repository.save(recipe)
        return recipe