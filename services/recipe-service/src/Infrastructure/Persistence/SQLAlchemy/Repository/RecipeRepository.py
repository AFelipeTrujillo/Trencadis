
from uuid import UUID
from typing import List
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.orm import selectinload

from Domain.Entity.Recipe import Recipe
from Domain.Repository.RecipeRepositoryInterface import RecipeRepositoryInterface
from Infrastructure.Persistence.SQLAlchemy.Models.RecipeModel import RecipeModel
from Infrastructure.Persistence.SQLAlchemy.Mappers.RecipeMapper import RecipeMapper

class RecipeRepository(RecipeRepositoryInterface):

    def __init__(self, session: AsyncSession):
        self.session = session
        

    async def save(self, recipe: Recipe):
        model = RecipeMapper.to_model(recipe)

        await self.session.merge(model)

        await self.session.flush()

    async def find_by_owner(self, owner_id: UUID) -> List[Recipe]:
        
        query = (
            select(RecipeModel)
            .where(RecipeModel.owner_id == owner_id)
            .options(selectinload(RecipeModel.ingredients))
        )

        result = await self.session.execute(query)

        models = result.scalars().all()

        return [RecipeMapper.to_domain(model) for model in models]
        
