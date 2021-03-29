"""empty message

Revision ID: 33568820fbd7
Revises: 
Create Date: 2021-03-30 01:29:36.953240

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '33568820fbd7'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('likelist',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('moviename', sa.VARCHAR(length=64), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('movie_model',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('moviename', sa.VARCHAR(length=64), nullable=False),
    sa.Column('year', sa.Integer(), nullable=True),
    sa.Column('rating', sa.Integer(), nullable=True),
    sa.Column('genre', sa.VARCHAR(length=128), nullable=False),
    sa.Column('summary', sa.VARCHAR(length=400), nullable=False),
    sa.Column('like_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['like_id'], ['likelist.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('movie_model')
    op.drop_table('likelist')
    # ### end Alembic commands ###
