"""beginning

Revision ID: 21725e4f6d5d
Revises: 
Create Date: 2021-04-13 09:52:19.044686

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '21725e4f6d5d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Orders',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('item', sa.Text(), nullable=True),
    sa.Column('dateyr', sa.Date(), nullable=True),
    sa.Column('datewk', sa.Date(), nullable=True),
    sa.Column('quantity', sa.Integer(), nullable=True),
    sa.Column('empid', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Orders')
    # ### end Alembic commands ###
