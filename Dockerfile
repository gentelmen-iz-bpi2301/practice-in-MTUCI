FROM python:3.9

WORKDIR /app

COPY . .

RUN pip install Flask requests

CMD ["python", "app.py"]

