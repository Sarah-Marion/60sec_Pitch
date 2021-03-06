"""Add a relationship between user and role model

Revision ID: 7b8b8e61b556
Revises: 88af6b884fe1
Create Date: 2018-05-21 10:41:14.036328

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7b8b8e61b556'
down_revision = '88af6b884fe1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('roles', sa.Column('user_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'roles', 'users', ['user_id'], ['id'])
    op.add_column('user_roles', sa.Column('user_id', sa.Integer(), nullable=True))
    op.drop_constraint('user_roles_user__id_fkey', 'user_roles', type_='foreignkey')
    op.create_foreign_key(None, 'user_roles', 'users', ['user_id'], ['id'])
    op.drop_column('user_roles', 'user__id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user_roles', sa.Column('user__id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'user_roles', type_='foreignkey')
    op.create_foreign_key('user_roles_user__id_fkey', 'user_roles', 'users', ['user__id'], ['id'])
    op.drop_column('user_roles', 'user_id')
    op.drop_constraint(None, 'roles', type_='foreignkey')
    op.drop_column('roles', 'user_id')
    # ### end Alembic commands ###
