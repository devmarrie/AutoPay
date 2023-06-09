"""Initial migration.

Revision ID: a9134c1a6bb9
Revises: c1d4e6e30866
Create Date: 2023-06-22 09:25:05.662464

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a9134c1a6bb9'
down_revision = 'c1d4e6e30866'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('history', schema=None) as batch_op:
        batch_op.drop_constraint('history_user_id_fkey', type_='foreignkey')
        batch_op.drop_column('user_id')

    with op.batch_alter_table('needs', schema=None) as batch_op:
        batch_op.add_column(sa.Column('phone_no', sa.String(length=60), nullable=False))
        batch_op.create_unique_constraint(None, ['phone_no'])
        batch_op.drop_constraint('needs_user_id_fkey', type_='foreignkey')
        batch_op.drop_column('user_id')

    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('email', sa.String(length=260), nullable=False))
        batch_op.drop_constraint('users_phone_no_key', type_='unique')
        batch_op.drop_column('phone_no')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('phone_no', sa.VARCHAR(length=60), autoincrement=False, nullable=False))
        batch_op.create_unique_constraint('users_phone_no_key', ['phone_no'])
        batch_op.drop_column('email')

    with op.batch_alter_table('needs', schema=None) as batch_op:
        batch_op.add_column(sa.Column('user_id', sa.VARCHAR(length=60), autoincrement=False, nullable=False))
        batch_op.create_foreign_key('needs_user_id_fkey', 'users', ['user_id'], ['id'])
        batch_op.drop_constraint(None, type_='unique')
        batch_op.drop_column('phone_no')

    with op.batch_alter_table('history', schema=None) as batch_op:
        batch_op.add_column(sa.Column('user_id', sa.VARCHAR(length=60), autoincrement=False, nullable=False))
        batch_op.create_foreign_key('history_user_id_fkey', 'users', ['user_id'], ['id'])

    # ### end Alembic commands ###
