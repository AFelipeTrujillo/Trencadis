# Recipe Service

## Domain

### Entities

#### Recipe

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

The **@dataclass** decorator is a utility provided by the dataclasses module that automatically generates special methods for a class, such as __init__(), __repr__(), and __eq__(), based on type hints. Its primary purpose is to reduce boilerplate code when creating classes that mainly serve as data containers.

### Value Objects

#### Ingredients

```python
from dataclasses import dataclass

@dataclass(frozen=True)
class Ingredient:
    name: str
    amount: float
    unit: str
```

The **frozen=True** parameter makes the instances of a dataclass immutable. Once an object is initialized, its fields cannot be assigned new values. This also makes the object hashable, allowing it to be used as a key in a dictionary or an element in a set.