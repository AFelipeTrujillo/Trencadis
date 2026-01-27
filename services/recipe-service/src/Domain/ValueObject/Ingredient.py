from dataclasses import dataclass
from Domain.ValueObject.MeasurementUnit import MeasurementUnit

"""
Represents an ingredient with a name, amount, and measurement unit.
frozen = True makes the dataclass immutable. 
"""
@dataclass(frozen=True)
class Ingredient:
    name: str
    amount: float
    unit: MeasurementUnit