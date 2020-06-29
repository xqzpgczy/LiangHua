"""empty message

Revision ID: 0ce9e3422f9e
Revises: 
Create Date: 2020-05-28 16:51:19.264044

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0ce9e3422f9e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('initial_quotas', table_name='plan')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index('initial_quotas', 'plan', ['initial_quotas'], unique=True)
    # ### end Alembic commands ###
