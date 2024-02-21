"""0008

Revision ID: 14f653c0820d
Revises: 4c200f8a6411
Create Date: 2024-02-21 09:38:43.310830

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '14f653c0820d'
down_revision: Union[str, None] = '4c200f8a6411'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('episodes', sa.Column('id', sa.Integer(), autoincrement=True, nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('episodes', 'id')
    # ### end Alembic commands ###