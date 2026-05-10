"""Create all performance indexes

Revision ID: 013
Revises: 012
Create Date: 2026-05-09

This migration runs last because indexes require the tables to already exist.
All 9 performance indexes are created here in one file.
"""
from alembic import op

revision = '013'
down_revision = '012'
branch_labels = None
depends_on = None


def upgrade():
    # Index 1: Coverage query - count verified workers per booth
    op.create_index(
        'idx_workers_party_verified_booth',
        'workers',
        ['party_id', 'verified', 'booth_id']
    )

    # Index 2: WhatsApp bot lookup - find worker by hashed phone number
    op.create_index(
        'idx_workers_phone_hash',
        'workers',
        ['phone_hash'],
        unique=True
    )

    # Index 3: Duplicate prevention - fast interval lookup (MOST IMPORTANT)
    op.create_index(
        'idx_reports_booth_election_interval',
        'turnoutreports',
        ['booth_id', 'election_id', 'interval'],
        unique=True
    )

    # Index 4: Prevent duplicate check-ins
    op.create_index(
        'idx_checkins_worker_election',
        'checkins',
        ['worker_id', 'election_id'],
        unique=True
    )

    # Index 5: Deployment coverage view - checked-in count per booth (queried every 30s)
    op.create_index(
        'idx_checkins_booth_election',
        'checkins',
        ['booth_id', 'election_id']
    )

    # Index 6: War room incident feed - all open critical incidents
    op.create_index(
        'idx_incidents_election_status_severity',
        'incidents',
        ['election_id', 'status', 'severity']
    )

    # Index 7: Unacknowledged alert feed - the core war room query
    op.create_index(
        'idx_alerts_constituency_election_ack',
        'alerts',
        ['constituency_id', 'election_id', 'acknowledged_at']
    )

    # Index 8: Alert engine idempotency - prevents duplicate alert firing
    op.create_index(
        'idx_alerts_booth_interval_type',
        'alerts',
        ['booth_id', 'election_id', 'interval', 'type'],
        unique=True
    )

    # Index 9: Read receipt deduplication / read rate computation
    op.create_index(
        'idx_broadcast_reads_broadcast_worker',
        'broadcastreads',
        ['broadcast_id', 'worker_id'],
        unique=True
    )


def downgrade():
    op.drop_index('idx_workers_party_verified_booth')
    op.drop_index('idx_workers_phone_hash')
    op.drop_index('idx_reports_booth_election_interval')
    op.drop_index('idx_checkins_worker_election')
    op.drop_index('idx_checkins_booth_election')
    op.drop_index('idx_incidents_election_status_severity')
    op.drop_index('idx_alerts_constituency_election_ack')
    op.drop_index('idx_alerts_booth_interval_type')
    op.drop_index('idx_broadcast_reads_broadcast_worker')
