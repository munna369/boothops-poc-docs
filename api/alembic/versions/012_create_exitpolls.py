"""Create exitpolls table

Revision ID: 012
Revises: 011
Create Date: 2026-05-09
"""
from alembic import op
import sqlalchemy as sa

revision = '012'
down_revision = '011'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'exitpolls',
        sa.Column('id', sa.UUID(as_uuid=True), primary_key=True,
                  server_default=sa.text('gen_random_uuid()')),
        sa.Column('booth_id', sa.UUID(as_uuid=True), nullable=False),
        sa.Column('election_id', sa.UUID(as_uuid=True), nullable=False),
        sa.Column('worker_id', sa.UUID(as_uuid=True), nullable=False),
        sa.Column('q1_answer', sa.Text, nullable=True),
        sa.Column('q2_answer', sa.Text, nullable=True),
        sa.Column('voter_refused', sa.Boolean, nullable=False, server_default='false'),
        sa.Column('created_at', sa.TIMESTAMP(timezone=True), nullable=False,
                  server_default=sa.text('NOW()')),
        sa.ForeignKeyConstraint(['booth_id'], ['booths.id'], ondelete='RESTRICT'),
        sa.ForeignKeyConstraint(['election_id'], ['elections.id'], ondelete='RESTRICT'),
        sa.ForeignKeyConstraint(['worker_id'], ['workers.id'], ondelete='RESTRICT'),
    )


def downgrade():
    op.drop_table('exitpolls')
