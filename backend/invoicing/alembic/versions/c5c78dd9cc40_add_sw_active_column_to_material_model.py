"""Add sw_active column to material model

Revision ID: c5c78dd9cc40
Revises: f0febe8404fb
Create Date: 2022-03-10 15:12:05.151941

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c5c78dd9cc40'
down_revision = 'f0febe8404fb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('material', sa.Column('sw_active', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('material', 'sw_active')
    # ### end Alembic commands ###
