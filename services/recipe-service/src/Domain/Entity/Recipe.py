# This file is part of the Domain layer of the application.
# It defines the Recipe entity with its attributes.
# It uses dataclasses for simplicity and type annotations for clarity.
from dataclasses import dataclass, field
from uuid import UUID, uuid4
from typing import List
from Domain.ValueObject.Ingredient import Ingredient
from Domain.Exception.IngredientAlreadyExistsException import IngredientAlreadyExistsException


@dataclass
class Recipe:
    name: str
    description: str
    owner_id: UUID
    # Automatically generate a unique identifier for each recipe
    id: UUID = field(default_factory=uuid4)
    ingredients: List[Ingredient] = field(default_factory=list)

    def add_ingredient(self, ingredient: Ingredient) -> None:
        """Adds an ingredient to the recipe."""
        if any(i.name == ingredient.name for i in self.ingredients):
            raise IngredientAlreadyExistsException(ingredient_name=ingredient.name)
        self.ingredients.append(ingredient)