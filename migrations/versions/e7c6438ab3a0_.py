"""empty message

Revision ID: e7c6438ab3a0
Revises:
Create Date: 2021-05-05 00:35:12.452443

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e7c6438ab3a0'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Movie')
    op.drop_table('Actor')
    # ### end Alembic commands ###
