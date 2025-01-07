FROM python:3.11

ENV POETRY_VERSION=2.0.0
ENV POETRY_HOME=/opt/poetry
ENV POETRY_VENV=/opt/poetry-venv
ENV POETRY_CACHE_DIR=/opt/.cache
ENV POETRY_NO_INTERACTION=1
ENV POETRY_VIRTUALENVS_CREATE=false

WORKDIR /code

COPY poetry.lock pyproject.toml ./
COPY source ./source

RUN curl -sSL https://install.python-poetry.org | python3 -

WORKDIR /code

RUN poetry install $(test "$ENVIRONMENT" == prod && echo "--only=main") --no-interaction --no-ansi
