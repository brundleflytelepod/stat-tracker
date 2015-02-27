"""empty message

Revision ID: bd93120755
Revises: 16bb593912
Create Date: 2015-02-26 23:34:18.058953

"""

# revision identifiers, used by Alembic.
revision = 'bd93120755'
down_revision = '16bb593912'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('activities', sa.Column('unit', sa.String(length=255), nullable=True))
    op.add_column('stat', sa.Column('ammount', sa.Integer(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('stat', 'ammount')
    op.drop_column('activities', 'unit')
    ### end Alembic commands ###