FROM python:3
LABEL maintainer="grimsleepless@protonmail.com"

WORKDIR /opt/code

ENV DATABASE_NAME=${DATABASE_NAME}
ENV DATABASE_USER=${DATABASE_USER}
ENV DATABASE_PASSWORD=${DATABASE_PASSWORD}

RUN apt update && apt install -y apt-utils build-essential curl && \
    pip install poetry

COPY entrypoint.sh /opt/code/
COPY pyproject.toml poetry.lock /opt/code/
RUN poetry config virtualenvs.create false && \
    poetry install --no-interaction --no-dev --no-ansi


COPY src/ /opt/code/
ENTRYPOINT ["./entrypoint.sh"]
