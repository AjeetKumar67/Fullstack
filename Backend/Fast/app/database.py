from sqlalchemy import create_engine, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Replace the placeholders with your MySQL database credentials
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:123456@localhost/fast"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def create_database():
    # Connect to MySQL server without specifying the database
    temp_engine = create_engine("mysql+pymysql://root:123456@localhost")
    with temp_engine.connect() as connection:
        connection.execute(text("CREATE DATABASE IF NOT EXISTS fast"))
        connection.close()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
