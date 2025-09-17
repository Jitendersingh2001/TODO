"""
Alembic command line interface
 -> alembic upgrade head
 -> alembic revision --autogenerate -m "name to describe the changes"
 -> alembic upgrade head # to apply the latest migration
 -> alembic downgrade -1 # to revert the last migration
 -> alembic history # to see the history of migrations
 -> alembic current # to see the current migration version
 -> alembic upgrade <Revision ID> # to upgrade to a specific migration
"""
