from sqlalchemy.orm import sessionmaker, DeclarativeBase
from sqlalchemy import create_engine


from config import DB_HOST, DB_NAME, DB_PASS, DB_PORT,DB_USER
from models import Base



DB_URL = f"postgresql://postgres:postgres@localhost:5432/postgres"

metadata = Base.metadata

engine = create_engine(DB_URL)
Session = sessionmaker(engine, expire_on_commit=False)
session = Session()