"""Create booths table

Revision ID: 004
Revises: 003
Create Date: 2026-05-09
"""
from alembic import op
import sqlalchemy as sa

revision = '004'
down_revision = '003'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'booths',
        sa.Column('id', sa.UUID(as_uuid=True), primary_key=True,
                  server_default=sa.text('gen_random_uuid()')),
        sa.Column('constituency_id', sa.UUID(as_uuid=True), nullable=False),
        sa.Column('booth_no', sa.String(20), nullable=False),
        sa.Column('booth_name', sa.String(200), nullable=False),
        sa.Column('address', sa.Text, nullable=True),
        sa.Column('lat', sa.Numeric(9, 6), nullable=True),
        sa.Column('lng', sa.Numeric(9, 6), nullable=True),
        sa.Column('total_voters', sa.Integer, nullable=False, server_default='0'),
        sa.Column('classification', sa.String(20), nullable=True),
        sa.Column('created_at', sa.TIMESTAMP(timezone=True), nullable=False,
                  server_default=sa.text('NOW()')),
        sa.ForeignKeyConstraint(['constituency_id'], ['constituencies.id'], ondelete='RESTRICT'),
    )


def downgrade():
    op.drop_table('booths')
