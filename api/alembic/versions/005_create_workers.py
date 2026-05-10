"""Create workers table

Revision ID: 005
Revises: 004
Create Date: 2026-05-09
"""
from alembic import op
import sqlalchemy as sa

revision = '005'
down_revision = '004'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'workers',
        sa.Column('id', sa.UUID(as_uuid=True), primary_key=True,
                  server_default=sa.text('gen_random_uuid()')),
        sa.Column('party_id', sa.UUID(as_uuid=True), nullable=False),
        sa.Column('booth_id', sa.UUID(as_uuid=True), nullable=True),  # nullable: assigned later
        sa.Column('name', sa.String(120), nullable=False),
        sa.Column('phone_hash', sa.String(64), nullable=False),  # SHA-256, never plaintext
        sa.Column('role', sa.String(40), nullable=False),
        sa.Column('fcm_token', sa.Text, nullable=True),  # push notifications
        sa.Column('verified', sa.Boolean, nullable=False, server_default='false'),
        sa.Column('deactivated', sa.Boolean, nullable=False, server_default='false'),
        sa.Column('activity_score', sa.Integer, nullable=False, server_default='0'),
        sa.Column('verified_at', sa.TIMESTAMP(timezone=True), nullable=True),
        sa.Column('created_at', sa.TIMESTAMP(timezone=True), nullable=False,
                  server_default=sa.text('NOW()')),
        sa.ForeignKeyConstraint(['party_id'], ['parties.id'], ondelete='RESTRICT'),
        sa.ForeignKeyConstraint(['booth_id'], ['booths.id'], ondelete='RESTRICT'),
    )


def downgrade():
    op.drop_table('workers')
