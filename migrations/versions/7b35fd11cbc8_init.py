"""init

Revision ID: 7b35fd11cbc8
Revises: 
Create Date: 2022-09-15 00:19:20.748599

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7b35fd11cbc8'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('currency',
    sa.Column('num_code', sa.Integer(), nullable=False),
    sa.Column('char_code', sa.String(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('value', sa.Float(), nullable=False),
    sa.Column('nominal', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('num_code'),
    sa.UniqueConstraint('char_code')
    )
    op.create_table('orders',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('num_order', sa.Integer(), nullable=False),
    sa.Column('cost', sa.Float(), nullable=False),
    sa.Column('delivery_date', sa.Date(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('orders')
    op.drop_table('currency')
    # ### end Alembic commands ###
