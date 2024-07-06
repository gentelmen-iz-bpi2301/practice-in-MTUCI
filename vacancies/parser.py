import requests
from core import session
from models import VacancyTable, Vacancy


def your_vacancies():
    URL='https://api.hh.ru/vacancies'
    response = requests.get(URL)
    if response.status_code == 200:
        data = response.json()
        vacancies = data.get("items", [])

    for vacancy in vacancies:
        post = vacancy.get('name')
        vacancy_url = vacancy.get('alternate_url')
        company = vacancy.get('employer', {}).get('name')
        salary = vacancy.get('salary')
        
        schedule = vacancy.get('schedule',{}).get('name')

        if salary:
            min_salary = salary.get('from', None)
            max_salary = salary.get('to', None)
            currency = salary.get('currency', None)

            if min_salary and max_salary:
                your_salary = f'{min_salary}-{max_salary} {currency}'
            elif min_salary:
                your_salary = f'от {min_salary}{currency}'   
            elif max_salary:
                your_salary = f'до {max_salary}{currency}'
            else:
                your_salary = 'Не указана'
        else:
            your_salary = 'Не указана'
        
        for vacancy in vacancies:
            parsed_vacancy = VacancyTable(
                post = post,
                salary = your_salary,
                company = company,
                schedule = schedule,
                vacancy_url = vacancy_url
            )
            session.add(parsed_vacancy)
            session.commit()
            return parsed_vacancy

