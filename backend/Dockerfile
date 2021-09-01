#syntax=docker/dockerfile:1

FROM python:3.9.5-slim-buster
WORKDIR /src
COPY requirements.txt requirements.txt
RUN pip3 install -r -U requirements.txt
COPY . .
CMD ["python3", "src/manage.py", "makemigrations"]
CMD ["python3", "src/manage.py", "migrate"]
CMD ["python3", "src/manage.py", "runserver"]