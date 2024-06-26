FROM python:3.11-slim-buster

RUN mkdir /code
WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./app /code/app
COPY ./data /code/data

EXPOSE 8000

CMD ["fastapi", "run", "app/main.py"]
