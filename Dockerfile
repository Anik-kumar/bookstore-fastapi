FROM python:3.11.4-slim-bullseye

RUN apt-get update && apt-get install -y gcc && apt-get clean

RUN mkdir -p /opt/fast-api-app

WORKDIR /opt/fast-api-app
RUN pip install --user poetry==1.5.1
ENV PATH="/root/.local/bin:${PATH}"
COPY poetry.lock /opt/fast-api-app/
COPY pyproject.toml /opt/fast-api-app/

RUN poetry install --no-dev

COPY src /opt/fast-api-app/src

CMD poetry run gunicorn src.main:app --workers 3 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:8081
