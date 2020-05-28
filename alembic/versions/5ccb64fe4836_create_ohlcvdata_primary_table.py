"""create_ohlcvdata_primary_table

Revision ID: 5ccb64fe4836
Revises: 461a3d615803
Create Date: 2020-05-28 10:09:16.860246

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5ccb64fe4836'
down_revision = '461a3d615803'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "ohlcvdata2",
        sa.Column('date', sa.DateTime()),
        sa.Column('Open', sa.DECIMAL(22, 8)),
        sa.Column('High', sa.DECIMAL(22, 8)),
        sa.Column('Low', sa.DECIMAL(22, 8)),
        sa.Column('Close', sa.DECIMAL(22, 8)),
        sa.Column('Volume', sa.DECIMAL(22, 8)),
        sa.Column('Market Cap', sa.DECIMAL(22, 8)),
    )


def downgrade():
    op.drop_table("ohlcvdata2")
