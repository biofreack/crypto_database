"""create ohlcvdata

Revision ID: 461a3d615803
Revises: 
Create Date: 2019-01-18 21:40:10.759141

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '461a3d615803'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "ohlcvdata",
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('cryptoid', sa.Integer()),
        sa.Column("name", sa.String(length=70)),
        sa.Column('event_date', sa.DateTime()),
        sa.Column('open', sa.DECIMAL(22,8)),
        sa.Column('high', sa.DECIMAL(22, 8)),
        sa.Column('low', sa.DECIMAL(22, 8)),
        sa.Column('close', sa.DECIMAL(22, 8)),
        sa.Column('volume', sa.DECIMAL(22, 8)),
        sa.Column('marketcap', sa.DECIMAL(22, 8)),
        sa.Column('import_date', sa.DateTime())
    )


def downgrade():
    op.drop_table("ohlcvdata")
