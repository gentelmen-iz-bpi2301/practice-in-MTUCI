from fastapi import FastAPI
from vacancies import router as vacancy_router
from core import init_db, session
from models import Vacancy

app = FastAPI(
    title = 'Vacancy Parser'
)

@app.get('/init_database')
def init_database():
    init_db()

@app.get('/vacancies')
def get_vacancies():
    vacancies = session.query(Vacancy).all()
    return vacancies

app.include_router(
    vacancy_router
)