from sqlalchemy.orm import mapped_column, Mapped
from .base import Base

class Vacancy(Base):
    __tablename__ = 'vacancy'


    post: Mapped[str] = mapped_column(nullable=False)
    salary: Mapped[str]
    requirements: Mapped[str]
    company: Mapped[str] = mapped_column(nullable=False)
    schedule: Mapped[str] = mapped_column(nullable=False)