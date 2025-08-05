FROM python:3.13-slim

WORKDIR /app/cashflow_service

# Установка системных зависимостей для psycopg2
RUN apt-get update && apt-get install -y \
    libpq-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# requirements.txt в контейнер
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Код проекта в контейнер
COPY . .

# Команда для запуска сервера Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]