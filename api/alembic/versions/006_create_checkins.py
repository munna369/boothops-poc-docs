"""Create checkins table

Revision ID: 006
Revises: 005
Create Date: 2026-05-09
"""
from alembic import op
import sqlalchemy as sa

revision = '006'
down_revision = '005'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'checkins',
        sa.Column('id', sa.UUID(as_uuid=True), primary_key=True,
                  server_default=sa.text('gen_random_uuid()')),
        sa.Column('worker_id', sa.UUID(as_uuid=True), nullable=False),
        sa.Column('booth_id', sa.UUID(as_uuid=True), nullable=False),
        sa.Column('election_id', sa.UUID(as_uuid=True), nullable=False),
        sa.Column('checkin_lat', sa.Numeric(9, 6), nullable=False),
        sa.Column('checkin_lng', sa.Numeric(9, 6), nullable=False),
        sa.Column('distance_meters', sa.Integer, nullable=False),
        sa.Column('valid', sa.Boolean, nullable=False),
        sa.Column('override_reason', sa.Text, nullable=True),
        sa.Column('checkin_time', sa.TIMESTAMP(timezone=True), nullable=False,
                  server_default=sa.text('NOW()')),
        sa.ForeignKeyConstraint(['worker_id'], ['workers.id'], ondelete='RESTRICT'),
        sa.ForeignKeyConstraint(['booth_id'], ['booths.id'], ondelete='RESTRICT'),
        sa.ForeignKeyConstraint(['election_id'], ['elections.id'], ondelete='RESTRICT'),
        sa.UniqueConstraint('worker_id', 'election_id', name='uq_checkin_worker_election'),
    )


def downgrade():
    op.drop_table('checkins')
