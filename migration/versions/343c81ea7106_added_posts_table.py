"""added posts table

Revision ID: 343c81ea7106
Revises: be555f908cbc
Create Date: 2023-01-01 21:14:59.389316

"""
from alembic import op
import sqlalchemy as sa
import sqlalchemy
from sqlalchemy import INTEGER, VARCHAR, NVARCHAR, Column, TIMESTAMP, func, ForeignKeyConstraint

# revision identifiers, used by Alembic.
revision = '343c81ea7106'
down_revision = 'be555f908cbc'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'posts',
        Column('id', INTEGER, primary_key=True),
        Column('title', VARCHAR(50), nullable=False),
        Column('body', VARCHAR(255)),
        Column('image', VARCHAR(200)),
        Column("creator_id", sa.Integer, sa.ForeignKey("users.id"), nullable=False),
        Column('created_at', TIMESTAMP, server_default=func.now()),
        Column('updated_at', TIMESTAMP, server_default=func.now(),onupdate=func.now())
    )
    
def downgrade() -> None:
    pass
