import pytest
from unittest.mock import Mock
from uuid import uuid4

from Domain.ValueObject.MeasurementUnit import MeasurementUnit
from Application.UseCase.CreateRecipeUseCase import CreateRecipeUseCase
from Application.DTO.RecipeDTOs import CreateRecepieRequest

def test_create_recipe_executes_successfully():

    mock_repo = Mock()
    use_case = CreateRecipeUseCase(repository=mock_repo)

    owner_id = uuid4()

    request_dto = CreateRecepieRequest(
        name="Test Recipe",
        description="A delicious test recipe",
        owner_id=owner_id,
        ingredients=[
            {
                "name": "Test Ingredient",
                "amount": 100.0,
                "unit": MeasurementUnit.GRAM
            }
        ]
    )

    result = use_case.execute(
        owner_id= owner_id , 
        request=request_dto
    )

    assert result.name == "Test Recipe"
    assert result.description == "A delicious test recipe"

    mock_repo.save.assert_called_once()
    save_arg = mock_repo.save.call_args[0][0]
    assert save_arg.name == "Test Recipe"