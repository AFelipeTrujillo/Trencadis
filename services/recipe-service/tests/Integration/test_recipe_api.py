import pytest
from uuid import UUID

@pytest.mark.asyncio
async def test_create_and_list_recipie_flow(client, override_auth, mock_user_id, db_session):
    recipe_payload = {
        # "id": "770e8400-e29b-41d4-a716-446655441111",
        "name": "Tortilla de Patatas",
        "description": "Un clásico de la cocina española",
        "ingredients": [
            {"name": "Patatas", "amount": 500, "unit": "g"},
            {"name": "Huevos", "amount": 6, "unit": "u"}
        ]
    }

    response = await client.post("/recipes", json=recipe_payload)

    assert response.status_code == 200
    assert response.json()["message"] == "Recipe created successfully"

    list_response = await client.get("/recipes")

    assert list_response.status_code == 200
    recipes = list_response.json()
    assert len(recipes) > 0

    created_recipe = recipes[0]
    assert "id" in created_recipe
    assert created_recipe["name"] == "Tortilla de Patatas" 