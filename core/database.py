from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, inspect
from models import Base



DB_URL = f"sqlite:///your_vaccacncies.db"

metadata = Base.metadata

engine = create_engine(DB_URL, echo=True)
Session = sessionmaker(engine, expire_on_commit=False)
session = Session()

inspector = inspect(engine)
tables = inspector.get_table_names()
if not tables:
    print('Нет таблиц')
else:
    print(f'Вот таблицы:{tables}')