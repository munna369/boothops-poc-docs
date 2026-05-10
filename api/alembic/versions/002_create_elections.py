"""Create elections table

Revision ID: 002
Revises: 001
Create Date: 2026-05-09
"""
from alembic import op
import sqlalchemy as sa

revision = '002'
down_revision = '001'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'elections',
        sa.Column('id', sa.UUID(as_uuid=True), primary_key=True,
                  server_default=sa.text('gen_random_uuid()')),
        sa.Column('party_id', sa.UUID(as_uuid=True), nullable=False),
        sa.Column('name', sa.String(200), nullable=False),
        sa.Column('election_date', sa.Date, nullable=False),
        sa.Column('polling_start', sa.Time, nullable=False, server_default='07:00'),
        sa.Column('polling_end', sa.Time, nullable=False, server_default='18:00'),
        sa.Column('status', sa.String(20), nullable=False, server_default='draft'),
        sa.Column('turnout_thresholds', sa.JSON, nullable=False,
                  server_default='{"09:00":10,"11:00":20,"13:00":35,"15:00":55}'),
        sa.Column('min_workers_per_booth', sa.Integer, nullable=False, server_default='2'),
        sa.Column('checkin_radius_meters', sa.Integer, nullable=False, server_default='200'),
        sa.Column('activated_at', sa.TIMESTAMP(timezone=True), nullable=True),
        sa.Column('locked_at', sa.TIMESTAMP(timezone=True), nullable=True),
        sa.Column('created_at', sa.TIMESTAMP(timezone=True), nullable=False,
                  server_default=sa.text('NOW()')),
        sa.ForeignKeyConstraint(['party_id'], ['parties.id'], ondelete='RESTRICT'),
    )


def downgrade():
    op.drop_table('elections')
