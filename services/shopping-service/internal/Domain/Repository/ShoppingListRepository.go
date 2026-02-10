package Repository

import (
	"context"

	"github.com/AFelipeTrujillo/Trencadis/internal/Domain/Entity"
	"github.com/google/uuid"
)

type ShoppingListRepository interface {
	Save(ctx context.Context, list *Entity.ShoppingList) error
	FindByID(ctx context.Context, id uuid.UUID) (*Entity.ShoppingList, error)
}
