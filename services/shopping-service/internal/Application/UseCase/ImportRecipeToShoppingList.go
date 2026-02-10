package UseCase

import (
	"context"

	"github.com/AFelipeTrujillo/Trencadis/internal/Domain/Repository"
	"github.com/google/uuid"
)

type ImportRecipeToShoppingList struct {
	repo Repository.ShoppingListRepository
}

func (uc *ImportRecipeToShoppingList) Execute(ctx context.Context, recipeID uuid.UUID, userID uuid.UUID) error {
	return nil
}
