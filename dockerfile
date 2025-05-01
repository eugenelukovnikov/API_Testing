# Официальный образ Python
FROM python:3.11-slim

ENV PYTHONPATH=/app

# Рабочая директория
WORKDIR /app

COPY requirements.txt .

# Устанавливаем системные зависимости 
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    git \
    wget \
    chromium-driver \
    && rm -rf /var/lib/apt/lists/*

# Устанавливаем Python-зависимости
# Альтернатива: RUN pip install --no-cache-dir pytest requests faker allure-pytest selenium
RUN pip install --no-cache-dir -r requirements.txt

# Копируем файлы проекта
COPY . .

# Команда для запуска тестов
CMD ["pytest", "-v", "--alluredir=./allure-results"]