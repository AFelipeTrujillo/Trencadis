"""Initial migration: Create recipes and ingredients tables

Revision ID: a73ddd483b13
Revises: 
Create Date: 2026-01-27 18:27:31.648239

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a73ddd483b13'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        'recipes',
        sa.Column('id', sa.UUID(), primary_key=True),
        sa.Column('name', sa.String(length=100), nullable=False),
        sa.Column('description', sa.Text(), nullable=True),
        sa.Column('owner_id', sa.UUID(), nullable=False, index=True)
    )

    op.create_table(
        'ingredients',
        sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column('recipe_id', sa.UUID(), sa.ForeignKey('recipes.id'), nullable=False, index=True),
        sa.Column('name', sa.String(length=100), nullable=False),
        sa.Column('amount', sa.Float(), nullable=False),
        sa.Column('unit', sa.String(length=50), nullable=False)
    )


def downgrade() -> None:
    """Downgrade schema."""
    pass
