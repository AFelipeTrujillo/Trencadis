from Domain.Exception.DomainException import DomainException

class IngredientAlreadyExistsException(DomainException):
    """Exception raised when trying to add an ingredient that already exists in the recipe."""
    def __init__(self, *args, ingredient_name: str = ""):
        message = f"Ingredient '{ingredient_name}' already exists in the recipe."
        super().__init__(message, *args)
         