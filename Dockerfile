# Используем базовый образ, содержащий Python
FROM python:3.8

# Устанавливаем зависимости, включая Streamlit
COPY requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install --no-cache-dir -r requirements.txt

# Копируем все файлы вашего приложения в контейнер
COPY . /app

# Запускаем ваше приложение
CMD ["streamlit", "run", "app/github_page.py"]
