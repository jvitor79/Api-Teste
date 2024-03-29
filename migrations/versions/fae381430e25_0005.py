"""0005

Revision ID: fae381430e25
Revises: ce929b243d3c
Create Date: 2024-02-20 14:30:45.969358

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'fae381430e25'
down_revision: Union[str, None] = 'ce929b243d3c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('episodes_season_fkey', 'episodes', type_='foreignkey')
    op.drop_column('episodes', 'season')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('episodes', sa.Column('season', sa.INTEGER(), autoincrement=False, nullable=False))
    op.create_foreign_key('episodes_season_fkey', 'episodes', 'seasons', ['season'], ['id'])
    # ### end Alembic commands ###
