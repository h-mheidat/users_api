"""Added Unique Constraint in Addresses table


Revision ID: 4b1fedbc08ac
Revises: 2b6cedb9caa1
Create Date: 2021-05-30 14:42:29.012983

"""

from alembic import op

# revision identifiers, used by Alembic.
revision = '4b1fedbc08ac'
down_revision = '2b6cedb9caa1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'addresses', ['zip_code', 'house_num'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'addresses', type_='unique')
    # ### end Alembic commands ###
