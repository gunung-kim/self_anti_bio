FROM python:3.12-slim

WORKDIR /app

COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv

COPY pyproject.toml uv.lock* ./
COPY alembic.ini .
RUN uv sync --frozen --no-dev

ENV PATH="/app/.venv/bin:$PATH"

COPY backend/app ./app

