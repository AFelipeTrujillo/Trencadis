# This file is part of the Domain layer of the application.
# It defines the Recipe entity with its attributes.
# It uses dataclasses for simplicity and type annotations for clarity.
from dataclasses import dataclass, field
# Importing UUID for unique identification of the recipe owner
from uuid import UUID, uuid4


@dataclass
class Recipe:
    name: str
    description: str
    owner_id: UUID
    # Automatically generate a unique identifier for each recipe
    id: UUID = field(default_factory=uuid4)
    ingredients: list[str] = field(default_factory=list)