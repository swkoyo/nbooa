"""Initial migration

Revision ID: 4d165c25195d
Revises: 
Create Date: 2023-04-05 14:05:50.228488

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4d165c25195d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('player',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('_id', sa.String(length=20), nullable=False),
    sa.Column('start_year', sa.String(length=4), nullable=False),
    sa.Column('end_year', sa.String(length=4), nullable=True),
    sa.Column('first_name', sa.String(length=150), nullable=False),
    sa.Column('last_name', sa.String(length=150), nullable=False),
    sa.Column('image_url', sa.String(length=255), nullable=False),
    sa.Column('birthday', sa.DateTime(), nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('player')
    # ### end Alembic commands ###
