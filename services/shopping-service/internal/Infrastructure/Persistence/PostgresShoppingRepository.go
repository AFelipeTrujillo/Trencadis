package Persistence

import (
	"context"

	"github.com/AFelipeTrujillo/Trencadis/internal/Domain/Entity"
	"github.com/jmoiron/sqlx"
)

type PostgresShoppingRepository struct {
	db *sqlx.DB
}

func (r *PostgresShoppingRepository) Save(ctx context.Context, list *Entity.ShoppingList) error {
	query := `INSERT INTO shopping_lists (id, user_id, name, status) VALUES (:id, :user_id, :name, :status)`
	_, err := r.db.NamedExecContext(ctx, query, list)
	return err
}
