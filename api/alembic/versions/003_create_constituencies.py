"""Create constituencies table

Revision ID: 003
Revises: 002
Create Date: 2026-05-09
"""
from alembic import op
import sqlalchemy as sa

revision = '003'
down_revision = '002'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'constituencies',
        sa.Column('id', sa.UUID(as_uuid=True), primary_key=True,
                  server_default=sa.text('gen_random_uuid()')),
        sa.Column('election_id', sa.UUID(as_uuid=True), nullable=False),
        sa.Column('party_id', sa.UUID(as_uuid=True), nullable=False),
        sa.Column('name', sa.String(200), nullable=False),
        sa.Column('ec_code', sa.String(20), nullable=True),
        sa.Column('state', sa.String(60), nullable=False),
        sa.Column('total_booths', sa.Integer, nullable=False, server_default='0'),
        sa.Column('total_voters', sa.Integer, nullable=False, server_default='0'),
        sa.Column('live_stats', sa.JSON, nullable=True),
        sa.Column('created_at', sa.TIMESTAMP(timezone=True), nullable=False,
                  server_default=sa.text('NOW()')),
        sa.ForeignKeyConstraint(['election_id'], ['elections.id'], ondelete='RESTRICT'),
        sa.ForeignKeyConstraint(['party_id'], ['parties.id'], ondelete='RESTRICT'),
    )


def downgrade():
    op.drop_table('constituencies')
