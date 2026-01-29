from abc import ABC, abstractmethod

from Application.UseCase.CreateRecipeUseCase import CreateRecipeUseCase
from Application.UseCase.ListRecipesUseCase import ListRecipesUseCase

class RecipeUseCaseFactoryInterface(ABC):
    """
    Interface for the Recipe Use Case Factory.
    
    This factory follows the Abstract Factory Pattern to centralize the creation 
    of use cases, ensuring that all dependencies (like repositories) are 
    correctly injected without leaking infrastructure details into the delivery layer.
    """

    @abstractmethod
    def create_create_recipe_use_case(self) -> CreateRecipeUseCase:
        """
        Initializes and returns an instance of CreateRecipeUseCase.
        
        Returns:
            CreateRecipeUseCase: The business logic for recipe creation.
        """
        pass

    @abstractmethod
    def create_list_recipes_use_case(self) -> ListRecipesUseCase:
        """
        Initializes and returns an instance of ListRecipesUseCase.
        
        Returns:
            ListRecipesUseCase: The business logic for retrieving recipes.
        """
        pass