"""Create turnoutreports table

Revision ID: 007
Revises: 006
Create Date: 2026-05-09
"""
from alembic import op
import sqlalchemy as sa

revision = '007'
down_revision = '006'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'turnoutreports',
        sa.Column('id', sa.UUID(as_uuid=True), primary_key=True,
                  server_default=sa.text('gen_random_uuid()')),
        sa.Column('booth_id', sa.UUID(as_uuid=True), nullable=False),
        sa.Column('election_id', sa.UUID(as_uuid=True), nullable=False),
        sa.Column('worker_id', sa.UUID(as_uuid=True), nullable=False),
        sa.Column('interval', sa.String(10), nullable=False),  # 09:00, 11:00 etc
        sa.Column('voter_count', sa.Integer, nullable=False),
        sa.Column('pct', sa.Numeric(5, 2), nullable=False),  # computed server-side
        sa.Column('channel', sa.String(20), nullable=False, server_default='app'),  # app,whatsapp,manual
        sa.Column('is_offline_sync', sa.Boolean, nullable=False, server_default='false'),
        sa.Column('reported_at', sa.TIMESTAMP(timezone=True), nullable=False),  # client time
        sa.Column('created_at', sa.TIMESTAMP(timezone=True), nullable=False,
                  server_default=sa.text('NOW()')),  # server time
        sa.ForeignKeyConstraint(['booth_id'], ['booths.id'], ondelete='RESTRICT'),
        sa.ForeignKeyConstraint(['election_id'], ['elections.id'], ondelete='RESTRICT'),
        sa.ForeignKeyConstraint(['worker_id'], ['workers.id'], ondelete='RESTRICT'),
        sa.UniqueConstraint('booth_id', 'election_id', 'interval',
                            name='uq_report_booth_election_interval'),
    )


def downgrade():
    op.drop_table('turnoutreports')
