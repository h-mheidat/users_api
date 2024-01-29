FROM python:3.9.0-slim-buster AS base

FROM base AS build

RUN apt update && \
    apt install libpq-dev gcc git -y

WORKDIR /tmp

ARG EXTRA_REQUIREMENTS

ENV PATH=/opt/local/bin:$PATH
ENV PIP_PREFIX=/opt/local
ENV PIP_DISABLE_PIP_VERSION_CHECK=1

COPY requirements.txt ./

RUN pip install -r requirements.txt

FROM base AS deploy

COPY --from=build /opt/local /opt/local
COPY --from=build /usr/lib/x86_64-linux-gnu/ /lib/x86_64-linux-gnu/ /usr/lib/

WORKDIR /app
COPY . /app

ENV PATH=/opt/local/bin:$PATH \
    PYTHONPATH=/opt/local/lib/python3.9/site-packages:/app \
    GUNICORN_CMD_ARGS=$GUNICORN_CMD_ARGS

EXPOSE 80

STOPSIGNAL SIGINT


CMD ["ddtrace-run", "gunicorn", "-b 0.0.0.0:8000", "main:app"]
