"""Create alerts table

Revision ID: 009
Revises: 008
Create Date: 2026-05-09
"""
from alembic import op
import sqlalchemy as sa

revision = '009'
down_revision = '008'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'alerts',
        sa.Column('id', sa.UUID(as_uuid=True), primary_key=True,
                  server_default=sa.text('gen_random_uuid()')),
        sa.Column('constituency_id', sa.UUID(as_uuid=True), nullable=False),
        sa.Column('booth_id', sa.UUID(as_uuid=True), nullable=False),
        sa.Column('election_id', sa.UUID(as_uuid=True), nullable=False),
        sa.Column('type', sa.String(40), nullable=False),
        sa.Column('severity', sa.String(20), nullable=False),
        sa.Column('threshold_pct', sa.Numeric(5, 2), nullable=False),
        sa.Column('actual_pct', sa.Numeric(5, 2), nullable=False),
        sa.Column('interval', sa.String(10), nullable=False),
        sa.Column('acknowledged_by', sa.UUID(as_uuid=True), nullable=True),
        sa.Column('resolution_note', sa.Text, nullable=True),
        sa.Column('triggered_at', sa.TIMESTAMP(timezone=True), nullable=False,
                  server_default=sa.text('NOW()')),
        sa.Column('acknowledged_at', sa.TIMESTAMP(timezone=True), nullable=True),
        sa.Column('resolved_at', sa.TIMESTAMP(timezone=True), nullable=True),
        sa.ForeignKeyConstraint(['constituency_id'], ['constituencies.id'], ondelete='RESTRICT'),
        sa.ForeignKeyConstraint(['booth_id'], ['booths.id'], ondelete='RESTRICT'),
        sa.ForeignKeyConstraint(['election_id'], ['elections.id'], ondelete='RESTRICT'),
        sa.ForeignKeyConstraint(['acknowledged_by'], ['workers.id'], ondelete='RESTRICT'),
        sa.UniqueConstraint('booth_id', 'election_id', 'interval', 'type',
                            name='uq_alert_booth_interval_type'),
    )


def downgrade():
    op.drop_table('alerts')
