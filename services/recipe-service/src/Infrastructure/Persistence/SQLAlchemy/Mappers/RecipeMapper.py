
from Domain.Entity.Recipe import Recipe
from Domain.Entity.Recipe import Ingredient
from Infrastructure.Persistence.SQLAlchemy.Models.RecipeModel import RecipeModel
from Infrastructure.Persistence.SQLAlchemy.Models.RecipeModel import IngredientModel


class RecipeMapper():

    @staticmethod
    def to_domain(model: RecipeModel) -> Recipe:
        
        ingredients = [
            Ingredient(
                name = ingredient.name,
                amount = ingredient.amount,
                unit = ingredient.unit
            ) for ingredient in model.ingredients
        ]

        return Recipe(
            id=model.id,
            name=model.name,
            description=model.description,
            owner_id=model.owner_id,
            ingredients=ingredients
        )
    
    @staticmethod
    def to_model(entity: Recipe) -> RecipeModel:
        
        ingredient_model = [
            IngredientModel(
                name = ingredient.name,
                amount = ingredient.amount,
                unit = ingredient.unit
            ) for ingredient in entity.ingredients
        ]

        return RecipeModel(
            id = entity.id,
            name = entity.name,
            description = entity.description,
            owner_id = entity.owner_id,
            ingredients = ingredient_model,
        )
