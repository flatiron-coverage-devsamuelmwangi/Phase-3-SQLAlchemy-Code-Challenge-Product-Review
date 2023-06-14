"""Create tables

Revision ID: 970a8aced6ba
Revises: 
Create Date: 2023-06-14 20:07:29.969692

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '970a8aced6ba'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'users',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_table(
        'products',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(), nullable=True),
        sa.Column('price', sa.Integer(), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_table(
        'reviews',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('star_rating', sa.Integer(), nullable=True),
        sa.Column('comment', sa.String(), nullable=True),
        sa.Column('user_id', sa.Integer(), nullable=True),
        sa.Column('product_id', sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
        sa.ForeignKeyConstraint(['product_id'], ['products.id'], ),
        sa.PrimaryKeyConstraint('id')
    )


# Downgrade function
def downgrade():
    op.drop_table('reviews')
    op.drop_table('products')
    op.drop_table('users')
