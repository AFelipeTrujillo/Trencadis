package Entity

import (
	"github.com/AFelipeTrujillo/Trencadis/internal/Domain/ValueObject"
	"github.com/google/uuid"
)

type ShoppingList struct {
	ID     uuid.UUID
	UserID uuid.UUID
	Name   string
	Status ValueObject.ListStatus
	Items  []ShoppingListItem
}

type ShoppingListItem struct {
	ID        uuid.UUID
	Name      string
	Quantity  float64
	Unit      string
	IsChecked bool
}
