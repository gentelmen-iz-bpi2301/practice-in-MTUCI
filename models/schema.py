from pydantic import BaseModel

class Vacancy(BaseModel):
    post: str
    salary: str
    requirements: str
    company: str
    schedule: str