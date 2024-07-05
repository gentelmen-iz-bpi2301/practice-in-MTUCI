from database import engine
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass

def init_db():
    try:
        Base.metadata.drop_all(engine)
        Base.metadata.create_all(engine)
        print("Database initialized successfully!")
    except Exception as e:
        print(f"Error initializing database: {e}")

init_db()