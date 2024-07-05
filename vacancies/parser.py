import requests
from bs4 import BeautifulSoup as bs


URL='https://hh.ru/vacancy/99989889?utm_medium=cpc_hh&utm_source=clickmehhru&utm_campaign=589940&utm_local_campaign=966235&utm_content=626304&utm_vacancy=99989889'
response = requests.get(URL)
print(response.status_code)