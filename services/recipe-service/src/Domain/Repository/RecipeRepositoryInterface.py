from abc import ABC, abstractmethod
from typing import Optional, List
from uuid import UUID
from Domain.Entity.Recipe import Recipe

class RecipeRepositoryInterface(ABC):

    @abstractmethod
    def save(self, recipe: Recipe):
        """ Saves a recipe to the repository. """
        pass

    @abstractmethod
    def find_by_id(self, recipe_id: UUID) -> Optional[Recipe]:
        """ Finds a recipe by its unique identifier. """
        pass

    @abstractmethod
    def find_by_owner(self, owner_id: UUID) -> List[Recipe]:
        """ Finds all recipes owned by a specific user. """
        pass