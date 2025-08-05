FROM python:3.13-slim

# Установка рабочей директории в корень проекта
WORKDIR /app

# Установка системных зависимостей для psycopg2
RUN apt-get update && apt-get install -y \
    libpq-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Копирование файла требований и их установка
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копирование всего кода проекта
COPY . .

# Команда для запуска сервера Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]