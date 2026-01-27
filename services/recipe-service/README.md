# Recipe Service - Trencadís

## Core Entities
- **Recipe**: The central aggregate root. It manages its own state and ensures business rules (like unique ingredients).

### Value Objects
- **Ingredient**: Immutable object (`frozen=True`) representing a component of a recipe.
- **MeasurementUnit**: Strongly typed enumeration for units (kg, g, l, etc.).

### Domain Contracts (Interfaces)
- **RecipeRepositoryInterface**: Abstract base class (ABC) that defines how recipes are persisted, decoupling the domain from the database technology.

### Exceptions
- **IngredientAlreadyExistsException**: Domain-specific error to prevent data inconsistency.

## Domain

### Entities

#### 1. Recipe

```python
from dataclasses import dataclass, field
from uuid import UUID, uuid4


@dataclass
class Recipe:
    name: str
    description: str
    owner_id: UUID
    # Automatically generate a unique identifier for each recipe
    id: UUID = field(default_factory=uuid4)
    ingredients: list[str] = field(default_factory=list)
    
```

**Notes**

> The **@dataclass** decorator is a utility provided by the dataclasses module that automatically generates special methods for a class, such as __init__(), __repr__(), and __eq__(), based on type hints. Its primary purpose is to reduce boilerplate code when creating classes that mainly serve as data containers.

### Value Objects

#### 1. Ingredients

```python
from dataclasses import dataclass
from Domain.ValueObject.MeasurementUnit import MeasurementUnit

@dataclass(frozen=True)
class Ingredient:
    name: str
    amount: float
    unit: MeasurementUnit
```

> The **frozen=True** parameter makes the instances of a dataclass immutable. Once an object is initialized, its fields cannot be assigned new values. This also makes the object hashable, allowing it to be used as a key in a dictionary or an element in a set.

#### 2. Measurement Unit

```python
from enum import Enum

class MeasurementUnit(Enum):
    KILOGRAM = "kg"
    GRAM = "g"
    POUND = "lb"
    OUNCE = "oz"
    LITER = "l"
    MILLILITER = "ml"
    GALLON = "gal"
    METER = "m"
    CENTIMETER = "cm"
    INCH = "in"
    FOOT = "ft"
    TEASPOON = "tsp"
    TABLESPOON = "tbsp"
```

**Notes**

> An **Enum (Enumeration)** is a symbolic name for a set of related constant values that are bound to unique identifiers. In Python, it is implemented as a class that inherits from enum.Enum, allowing you to group related constants together to improve code readability, prevent errors from misspelled strings (typos), and provide a clear structure for variables that should only take one of a predefined set of values.


### Repositories

#### 1. RecipeRepositoryInterface

```python
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
```

**Notes:**

> In Python, the abc module provides the infrastructure for defining **Abstract Base Classes (ABCs)**. An ABC is a class that cannot be instantiated on its own; instead, it defines a common blueprint or contract that all its subclasses must follow.

### Exceptions

#### 1. IngredientAlreadyExistsException

Exception raised when trying to add an ingredient that already exists in the recipe.

```python
from Domain.Exception.DomainException import DomainException

class IngredientAlreadyExistsException(DomainException):
    """Exception raised when trying to add an ingredient that already exists in the recipe."""
    def __init__(self, *args, ingredient_name: str = ""):
        message = f"Ingredient '{ingredient_name}' already exists in the recipe."
        super().__init__(message, *args)
```

## Security & Identity
This service acts as an **OAuth2 Resource Server**.
- **Provider**: Keycloak (OIDC).
- **Authentication**: JWT validation via `auth_guard`.
- **Authorization**: Extracts `owner_id` from the token's `sub` claim to ensure data isolation.

## Infrastructure

### Technology Stack
- **Python 3.11+**
- **FastAPI** (Web Framework)
- **Pydantic v2** (Data Validation)
- **Pytest** (Testing)

## Development

- **Local Setup**: Install dependencies using `pip install -e .`
- **Run Tests**: Execute pytest in the root directory.
- **API Docs**: Accessible at http://localhost:8001/docs when running via Docker.