"""empty message

Revision ID: dd22071d9a3e
Revises: 
Create Date: 2019-04-16 10:41:33.961665

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dd22071d9a3e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('media',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('filename', sa.String(length=250), nullable=False),
    sa.Column('file_url', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('media')
    # ### end Alembic commands ###
