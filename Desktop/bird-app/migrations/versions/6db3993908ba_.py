"""empty message

Revision ID: 6db3993908ba
Revises: d38777150e3f
Create Date: 2023-08-11 18:33:38.472104

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6db3993908ba'
down_revision = 'd38777150e3f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('products',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('product_name', sa.String(), nullable=False),
    sa.Column('product_category', sa.String(), nullable=False),
    sa.Column('price', sa.Double(), nullable=False),
    sa.Column('product_quantity', sa.Integer(), nullable=False),
    sa.Column('image', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('fname', sa.String(), nullable=False),
    sa.Column('lname', sa.String(), nullable=False),
    sa.Column('username', sa.String(), nullable=False),
    sa.Column('password', sa.String(), nullable=False),
    sa.Column('address', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('username')
    )
    op.create_table('transactions',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('transaction_date', sa.DateTime(), nullable=True),
    sa.Column('transaction_code', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('product_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['product_id'], ['products.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('birds')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('birds',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('species', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='birds_pkey')
    )
    op.drop_table('transactions')
    op.drop_table('users')
    op.drop_table('products')
    # ### end Alembic commands ###
