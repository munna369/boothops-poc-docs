"""Create incidents table

Revision ID: 008
Revises: 007
Create Date: 2026-05-09
"""
from alembic import op
import sqlalchemy as sa

revision = '008'
down_revision = '007'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'incidents',
        sa.Column('id', sa.UUID(as_uuid=True), primary_key=True,
                  server_default=sa.text('gen_random_uuid()')),
        sa.Column('booth_id', sa.UUID(as_uuid=True), nullable=False),
        sa.Column('election_id', sa.UUID(as_uuid=True), nullable=False),
        sa.Column('worker_id', sa.UUID(as_uuid=True), nullable=False),  # reporter
        sa.Column('type', sa.String(40), nullable=False),
        sa.Column('severity', sa.String(20), nullable=False),
        sa.Column('description', sa.Text, nullable=True),
        sa.Column('status', sa.String(20), nullable=False, server_default='reported'),
        sa.Column('media_keys', sa.ARRAY(sa.Text), nullable=True),  # S3 photo keys
        sa.Column('lat', sa.Numeric(9, 6), nullable=True),
        sa.Column('lng', sa.Numeric(9, 6), nullable=True),
        sa.Column('acknowledged_by', sa.UUID(as_uuid=True), nullable=True),  # FK to workers
        sa.Column('resolved_by', sa.UUID(as_uuid=True), nullable=True),  # FK to workers
        sa.Column('legal_ref', sa.String(100), nullable=True),
        sa.Column('acknowledged_at', sa.TIMESTAMP(timezone=True), nullable=True),
        sa.Column('resolved_at', sa.TIMESTAMP(timezone=True), nullable=True),
        sa.Column('created_at', sa.TIMESTAMP(timezone=True), nullable=False,
                  server_default=sa.text('NOW()')),
        sa.ForeignKeyConstraint(['booth_id'], ['booths.id'], ondelete='RESTRICT'),
        sa.ForeignKeyConstraint(['election_id'], ['elections.id'], ondelete='RESTRICT'),
        sa.ForeignKeyConstraint(['worker_id'], ['workers.id'], ondelete='RESTRICT'),
        sa.ForeignKeyConstraint(['acknowledged_by'], ['workers.id'], ondelete='RESTRICT'),
        sa.ForeignKeyConstraint(['resolved_by'], ['workers.id'], ondelete='RESTRICT'),
    )


def downgrade():
    op.drop_table('incidents')
