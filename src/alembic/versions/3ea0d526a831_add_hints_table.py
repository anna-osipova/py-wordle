"""Add hints table

Revision ID: 3ea0d526a831
Revises: e85c7fdd5d7a
Create Date: 2022-04-24 14:01:16.285830

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '3ea0d526a831'
down_revision = 'e85c7fdd5d7a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('hints',
                    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
                    sa.Column('guess_id', sa.Integer(), nullable=False),
                    sa.Column('letter', sa.String(length=1), nullable=False),
                    sa.Column('color', sa.Enum('GREY', 'YELLOW', 'GREEN', name='color'), nullable=False),
                    sa.ForeignKeyConstraint(['guess_id'], ['guesses.id'], ),
                    sa.PrimaryKeyConstraint('id')
                    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('hints')
    # ### end Alembic commands ###
