#!/usr/bin/env bash

alembic upgrade head
# ddtrace-run gunicorn -c gunicorn_conf.py src.main:app
uvicorn --reload --workers 1 --host 0.0.0.0 --port 80 src.main:app
