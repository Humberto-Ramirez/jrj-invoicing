"""Add audit

Revision ID: 66647fbe6d21
Revises: e90f7783453b
Create Date: 2022-03-10 14:24:08.238764

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '66647fbe6d21'
down_revision = 'e90f7783453b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('product', sa.Column('create_date', sa.DateTime(), nullable=False))
    op.add_column('product', sa.Column('last_modified', sa.DateTime(), nullable=True))
    op.drop_column('product', 'creation_date')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('product', sa.Column('creation_date', sa.DATE(), autoincrement=False, nullable=False))
    op.drop_column('product', 'last_modified')
    op.drop_column('product', 'create_date')
    # ### end Alembic commands ###
