
from unittest.mock import Mock
from uuid import uuid4

from Domain.Entity.Recipe import Recipe
from Application.DTO.RecipeDTOs import RecipeListResponse
from Application.UseCase.ListRecipesUseCase import ListRecipesUseCase


def test_list_recipes_executes_successfully():
    mock_repo = Mock()
    use_case = ListRecipesUseCase(repository=mock_repo)

    owner_id = uuid4()

    recipe_1 = Recipe(
        id=uuid4(),
        name="Recipe 1",
        description="First recipe",
        owner_id=owner_id,
        ingredients=[]
    )

    recipe_2 = Recipe(
        id=uuid4(),
        name="Recipe 2",
        description="Second recipe",
        owner_id=owner_id,
        ingredients=[]
    )
    
    mock_repo.find_by_owner.return_value = [
        recipe_1, 
        recipe_2
    ]

    result = use_case.execute(owner_id=owner_id)

    assert len(result) == 2
    assert result[0].name == "Recipe 1"
    assert result[1].name == "Recipe 2"

    mock_repo.find_by_owner.assert_called_once_with(owner_id)