from sqlalchemy import create_engine, inspect
from database import Base, engine
import models

# Inspect the database
inspector = inspect(engine)

# Get table names
existing_tables = inspector.get_table_names()

if existing_tables:
     print("Tables already exist, skipping table creation")
else:
     # Create tables
     print("Creating tables")
     Base.metadata.create_all(bind=engine)
     print("Tables created")

