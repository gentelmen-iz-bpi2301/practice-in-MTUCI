from fastapi import APIRouter
from .parser import your_vacancies
from models import VacancyTable

router = APIRouter(
    prefix='/vacancy_parser'
)

@router.post('/parser')
def vacancy():
    return your_vacancies()