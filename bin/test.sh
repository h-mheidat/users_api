#!/usr/bin/env bash

flake8 && isort --check --diff .
pytest
