from fastapi import APIRouter
from .parser_and_filter import your_vacancies, vacancy_filter


router = APIRouter(
    prefix='/vacancy_parser'
)

@router.post('/parser')
def vacancy():
    return your_vacancies()

@router.get('/filter')
def filter(post=None, salary=None, schedule=None):
    return vacancy_filter(post=post, salary=salary, schedule=schedule)
