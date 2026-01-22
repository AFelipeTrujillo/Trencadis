from dataclasses import dataclass
from Domain.ValueObject.MeasurementUnit import MeasurementUnit

@dataclass(frozen=True)
class Ingredient:
    name: str
    amount: float
    unit: MeasurementUnit