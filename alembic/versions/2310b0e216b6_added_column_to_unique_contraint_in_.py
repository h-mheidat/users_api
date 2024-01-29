"""Added column to unique contraint in Addresses table

Revision ID: 2310b0e216b6
Revises: 4b1fedbc08ac
Create Date: 2021-05-30 14:49:36.640797

"""
from alembic import op

# revision identifiers, used by Alembic.
revision = '2310b0e216b6'
down_revision = '4b1fedbc08ac'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('addresses_zip_code_house_num_key', 'addresses', type_='unique')
    op.create_unique_constraint(None, 'addresses', ['zip_code', 'state', 'house_num'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'addresses', type_='unique')
    op.create_unique_constraint('addresses_zip_code_house_num_key',
                                'addresses', ['zip_code', 'house_num'])
    # ### end Alembic commands ###
