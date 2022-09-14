FROM python:alpine as base
ENV PYTHONFAULTHANDLER=1 \
    PYTHONHASHSEED=random \
    PYTHONUNBUFFERED=1
WORKDIR /app


FROM base as builder
ENV PIP_DEFAULT_TIMEOUT=100 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_NO_CACHE_DIR=1 \
    POETRY_VERSION=1.2.0

RUN apk add --no-cache gcc libffi-dev musl-dev postgresql-dev g++
RUN pip install "poetry==$POETRY_VERSION"
RUN python -m venv /venv

COPY pyproject.toml poetry.lock ./
RUN poetry export -f requirements.txt --output requirements.txt
RUN /venv/bin/pip install -r requirements.txt
COPY ./app ./app
RUN poetry build && /venv/bin/pip install dist/*.whl


FROM base as final
MAINTAINER Novoseltcev Stanislav <novoseltcev.stanislav@gmail.com>
RUN apk add --no-cache libffi libpq
RUN ln -s /usr/share/zoneinfo/Europe/Moscow /etc/localtime
COPY --from=builder /venv /venv
COPY migrations ./migrations

COPY docker-entrypoint.sh wsgi.py ./
RUN chmod 777 docker-entrypoint.sh

#Configurate Crontab
COPY cron-entrypoint.sh ./
RUN chmod 777 cron-entrypoint.sh
COPY crontab /etc/cron.d/shedule
RUN chmod 0644 /etc/cron.d/shedule && crontab /etc/cron.d/shedule

CMD ["./docker-entrypoint.sh"]