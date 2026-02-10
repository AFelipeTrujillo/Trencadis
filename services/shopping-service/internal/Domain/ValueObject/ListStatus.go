package ValueObject

import (
	"errors"
	"fmt"
)

type ListStatus struct {
	value string
}

// ListStatus constants represent the available lifecycle states of a list.
// Using a struct-based approach ensures type safety across the application.
var (
	// StatusActive indicates the list is currently visible and modifiable.
	StatusActive = ListStatus{"active"}

	// StatusArchived indicates the list is hidden from the main view
	// but preserved for historical or recovery purposes.
	StatusArchived = ListStatus{"archived"}
)

var ErrInvalidStatus = errors.New("invalid shopping list status")

func NewListStatus(value string) (ListStatus, error) {
	switch value {
	case StatusActive.value, StatusArchived.value:
		return ListStatus{value: value}, nil
	default:
		return ListStatus{}, fmt.Errorf("%w: %s", ErrInvalidStatus, value)
	}
}
