from pydantic import BaseModel


class VacancyTable(BaseModel):
    post: str = ''
    salary: str = ''
    
    company: str = ''
    schedule: str = ''
    vacancy_url: str = ''


    