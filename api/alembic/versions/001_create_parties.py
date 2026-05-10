"""Create parties table

Revision ID: 001
Revises: 
Create Date: 2026-05-09
"""
from alembic import op
import sqlalchemy as sa

revision = '001'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'parties',
        sa.Column('id', sa.UUID(as_uuid=True), primary_key=True,
                  server_default=sa.text('gen_random_uuid()')),
        sa.Column('name', sa.String(120), nullable=False),
        sa.Column('slug', sa.String(40), nullable=False, unique=True),
        sa.Column('logo_url', sa.Text, nullable=True),
        sa.Column('primary_color', sa.String(7), nullable=True),
        sa.Column('subscription_tier', sa.String(20), nullable=False,
                  server_default='starter'),
        sa.Column('created_at', sa.TIMESTAMP(timezone=True), nullable=False,
                  server_default=sa.text('NOW()')),
    )


def downgrade():
    op.drop_table('parties')
