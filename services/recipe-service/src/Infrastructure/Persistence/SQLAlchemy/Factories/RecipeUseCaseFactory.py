from sqlalchemy.ext.asyncio import AsyncSession

from Application.Factory.RecipeUseCaseFactoryInterface import RecipeUseCaseFactoryInterface
from Application.UseCase.CreateRecipeUseCase import CreateRecipeUseCase
from Application.UseCase.ListRecipesUseCase import ListRecipesUseCase
from Infrastructure.Persistence.SQLAlchemy.Repository.RecipeRepository import RecipeRepository as SQLAlchemyRecipeRepository

class RecipeUseCaseFactory(RecipeUseCaseFactoryInterface):

    def __init__(self, session: AsyncSession):
        self.session = session

    def create_create_recipe_use_case(self) -> CreateRecipeUseCase:
        repository = SQLAlchemyRecipeRepository(self.session)
        return CreateRecipeUseCase(repository)
    
    def create_list_recipes_use_case(self) -> ListRecipesUseCase:
        repository = SQLAlchemyRecipeRepository(self.session)
        return ListRecipesUseCase(repository)