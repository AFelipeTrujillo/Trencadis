from uuid import UUID
from typing import List

from Infrastructure.Persistence.Database import Base

from sqlalchemy import String, Text, ForeignKey, Float
from sqlalchemy.orm import Mapped, mapped_column, relationship

class RecipeModel(Base):
    __tablename__ = "recipes"

    id: Mapped[UUID] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=True)
    owner_id: Mapped[UUID] = mapped_column(nullable=False, index=True)

    ingredients: Mapped[List["IngredientModel"]] = relationship(
        "IngredientModel",
        # back_populates must match the attribute name in IngredientModel
        back_populates="recipe",
        # delete-orphan to remove ingredients when recipe is deleted
        cascade="all, delete-orphan",
        # lazy="selectin" for efficient loading of related ingredients
        lazy="selectin"
    )
"""
Line Item for Recipe
Represents an ingredient in a recipe
Includes foreign key relationship to RecipeModel
"""
class IngredientModel(Base):
    __tablename__ = "ingredients"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)

    recipe_id: Mapped[UUID] = mapped_column(
        ForeignKey("recipes.id"), 
        nullable=False, 
        index=True
    )

    name: Mapped[str] = mapped_column(String(100), nullable=False)
    amount: Mapped[float] = mapped_column(Float, nullable=False)
    unit: Mapped[str] = mapped_column(String(50), nullable=False)

    recipe: Mapped["RecipeModel"] = relationship(
        "RecipeModel",
        back_populates="ingredients",
        # lazy = joined for eager loading of the recipe when loading an ingredient
        lazy="joined"
    )
    