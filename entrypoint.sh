#!/bin/bash
set -e

cd /app

uv run alembic upgrade head

exec uv run fastapi run src/main.py
