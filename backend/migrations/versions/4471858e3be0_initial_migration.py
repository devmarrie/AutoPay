"""Initial migration.

Revision ID: 4471858e3be0
Revises: a9134c1a6bb9
Create Date: 2023-06-22 14:32:23.870250

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '4471858e3be0'
down_revision = 'a9134c1a6bb9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('pay', schema=None) as batch_op:
        batch_op.add_column(sa.Column('number', sa.String(length=100), nullable=False))
        batch_op.add_column(sa.Column('code', sa.String(length=100), nullable=False))
        batch_op.add_column(sa.Column('need', sa.String(length=60), nullable=False))
        batch_op.drop_column('transaction_date')
        batch_op.drop_column('mpesano')
        batch_op.drop_column('mpesa_receipt_number')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('pay', schema=None) as batch_op:
        batch_op.add_column(sa.Column('mpesa_receipt_number', sa.VARCHAR(length=100), autoincrement=False, nullable=False))
        batch_op.add_column(sa.Column('mpesano', sa.INTEGER(), autoincrement=False, nullable=False))
        batch_op.add_column(sa.Column('transaction_date', postgresql.TIMESTAMP(), autoincrement=False, nullable=False))
        batch_op.drop_column('need')
        batch_op.drop_column('code')
        batch_op.drop_column('number')

    # ### end Alembic commands ###
