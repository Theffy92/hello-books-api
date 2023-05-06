"""Add Genre model

Revision ID: 822f44b17d89
Revises: 3e9e49475428
Create Date: 2023-05-05 23:24:51.586916

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '822f44b17d89'
down_revision = '3e9e49475428'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('genre',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('genre')
    # ### end Alembic commands ###
