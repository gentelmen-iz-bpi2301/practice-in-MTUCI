from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import Column, Integer, String, Text
from .base import Base

class Vacancy(Base):
    __tablename__ = 'your_vacancies'
    
    id = Column(Integer, primary_key=True, nullable=False, unique=True, autoincrement=True)
    post = Column(String, nullable=False)
    salary = Column(String)
    company = Column(String, nullable=False)
    schedule = Column(String, nullable=False)
    vacancy_url = Column(String, nullable=False)