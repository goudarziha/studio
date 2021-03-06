"""empty message

Revision ID: 4eda30af3d08
Revises: 465a85714133
Create Date: 2019-04-24 21:17:54.436880

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4eda30af3d08'
down_revision = '465a85714133'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('email', sa.Column('api_id', sa.Integer(), nullable=True))
    op.add_column('email', sa.Column('is_posted', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('email', 'is_posted')
    op.drop_column('email', 'api_id')
    # ### end Alembic commands ###
