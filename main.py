from fastapi import FastAPI
from vacancies import router as vacancy_router
from core import init_db

app = FastAPI(
    title = 'Vacancy Parser'
)

@app.get('/init_database')
def init_database():
    init_db()
    
app.include_router(
    vacancy_router
)