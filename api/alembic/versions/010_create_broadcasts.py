"""Create broadcasts table

Revision ID: 010
Revises: 009
Create Date: 2026-05-09
"""
from alembic import op
import sqlalchemy as sa

revision = '010'
down_revision = '009'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'broadcasts',
        sa.Column('id', sa.UUID(as_uuid=True), primary_key=True,
                  server_default=sa.text('gen_random_uuid()')),
        sa.Column('sender_id', sa.UUID(as_uuid=True), nullable=False),  # FK to workers
        sa.Column('constituency_id', sa.UUID(as_uuid=True), nullable=False),
        sa.Column('election_id', sa.UUID(as_uuid=True), nullable=False),
        sa.Column('message', sa.Text, nullable=False),
        sa.Column('channel', sa.String(20), nullable=False),
        sa.Column('recipient_count', sa.Integer, nullable=False),
        sa.Column('sent_at', sa.TIMESTAMP(timezone=True), nullable=False,
                  server_default=sa.text('NOW()')),
        sa.ForeignKeyConstraint(['sender_id'], ['workers.id'], ondelete='RESTRICT'),
        sa.ForeignKeyConstraint(['constituency_id'], ['constituencies.id'], ondelete='RESTRICT'),
        sa.ForeignKeyConstraint(['election_id'], ['elections.id'], ondelete='RESTRICT'),
    )


def downgrade():
    op.drop_table('broadcasts')
