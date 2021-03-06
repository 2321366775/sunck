"""第二次迁移

Revision ID: 3694fa739aac
Revises: bb58a6281d3f
Create Date: 2019-06-05 16:42:26.842060

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '3694fa739aac'
down_revision = 'bb58a6281d3f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index(op.f('ix_post_timestamp'), 'post', ['timestamp'], unique=False)
    op.add_column('user', sa.Column('password_hash', sa.String(length=128), nullable=True))
    op.add_column('user', sa.Column('username', sa.String(length=64), nullable=True))
    op.create_index(op.f('ix_user_username'), 'user', ['username'], unique=True)
    op.drop_index('ix_user_nickname', table_name='user')
    op.drop_column('user', 'nickname')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('nickname', mysql.VARCHAR(length=64), nullable=True))
    op.create_index('ix_user_nickname', 'user', ['nickname'], unique=True)
    op.drop_index(op.f('ix_user_username'), table_name='user')
    op.drop_column('user', 'username')
    op.drop_column('user', 'password_hash')
    op.drop_index(op.f('ix_post_timestamp'), table_name='post')
    # ### end Alembic commands ###
