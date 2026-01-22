from Domain.Repository.RecipeRepositoryInterface import RecipeRepositoryInterface
from Domain.Entity.Recipe import Recipe
from uuid import UUID

class InMemoryRecipeRepository(RecipeRepositoryInterface):
    def __init__(self):
        self.recipes = {}

    def save(self, recipe: Recipe):
        self.recipes[recipe.id] = recipe

    def find_by_id(self, recipe_id: UUID):
        return self.recipes.get(recipe_id)

    def find_by_owner(self, owner_id: UUID):
        return [recipe for recipe in self.recipes.values() if recipe.owner_id == owner_id]