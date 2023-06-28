"""Add name and description columns to poket_flows table

Revision ID: 872475c91f71
Revises: c92840d12a5a
Create Date: 2023-06-28 13:50:19.868156

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '872475c91f71'
down_revision = 'c92840d12a5a'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('pocket_flows', sa.Column('name', sa.String(), nullable=True))
    op.add_column('pocket_flows', sa.Column('description', sa.Text(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('pocket_flows', 'description')
    op.drop_column('pocket_flows', 'name')
    # ### end Alembic commands ###
