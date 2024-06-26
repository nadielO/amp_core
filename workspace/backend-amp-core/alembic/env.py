from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from alembic import context
import os
import sys
sys.path.append(os.getcwd())  # Include the root project directory to the sys.path

from app.db.base import Base  # Import the Base metadata
from app.core.config import settings  # Import settings

config = context.config
fileConfig(config.config_file_name)

# Override the sqlalchemy.url provided from the alembic.ini with the one from settings
config.set_main_option('sqlalchemy.url', settings.DATABASE_URL)

target_metadata = Base.metadata

def run_migrations_offline():
    url = config.get_main_option("sqlalchemy.url")
    context.configure(url=url, target_metadata=target_metadata, literal_binds=True, dialect_opts={"paramstyle": "named"})
    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online():
    connectable = engine_from_config(config.get_section(config.config_ini_section), prefix='sqlalchemy.', poolclass=pool.NullPool)
    context.configure(connectable=connectable, target_metadata=target_metadata)
    with context.begin_transaction():
        context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()