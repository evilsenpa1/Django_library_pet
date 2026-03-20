# ─────────────────────────────────────────
# Base image
# ─────────────────────────────────────────
FROM python:3.12-slim

# Не писать .pyc файлы, не буферизовать stdout/stderr
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# ─────────────────────────────────────────
# Системные зависимости для psycopg3
# ─────────────────────────────────────────
RUN apt-get update && apt-get install -y --no-install-recommends \
    libpq-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# ─────────────────────────────────────────
# Python зависимости
# ─────────────────────────────────────────
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# ─────────────────────────────────────────
# Копируем проект
# ─────────────────────────────────────────
COPY . .

EXPOSE 8000
