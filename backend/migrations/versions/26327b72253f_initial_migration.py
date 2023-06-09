"""Initial migration.

Revision ID: 26327b72253f
Revises: 088f64c0823f
Create Date: 2023-06-12 09:18:16.514165

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '26327b72253f'
down_revision = '088f64c0823f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('needs', schema=None) as batch_op:
        batch_op.drop_column('reminderdate')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('needs', schema=None) as batch_op:
        batch_op.add_column(sa.Column('reminderdate', postgresql.TIMESTAMP(), autoincrement=False, nullable=False))

    # ### end Alembic commands ###
