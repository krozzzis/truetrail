#!/bin/bash
set -e

cd /app

exec uv run src/main.py
