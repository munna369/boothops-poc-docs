"""Create broadcastreads table

Revision ID: 011
Revises: 010
Create Date: 2026-05-09
"""
from alembic import op
import sqlalchemy as sa

revision = '011'
down_revision = '010'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'broadcastreads',
        sa.Column('id', sa.UUID(as_uuid=True), primary_key=True,
                  server_default=sa.text('gen_random_uuid()')),
        sa.Column('broadcast_id', sa.UUID(as_uuid=True), nullable=False),
        sa.Column('worker_id', sa.UUID(as_uuid=True), nullable=False),
        sa.Column('read_at', sa.TIMESTAMP(timezone=True), nullable=False),
        sa.ForeignKeyConstraint(['broadcast_id'], ['broadcasts.id'], ondelete='RESTRICT'),
        sa.ForeignKeyConstraint(['worker_id'], ['workers.id'], ondelete='RESTRICT'),
        sa.UniqueConstraint('broadcast_id', 'worker_id', name='uq_broadcast_read'),
    )


def downgrade():
    op.drop_table('broadcastreads')
