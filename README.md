# NeuroBot Flask

Это простой чат-бот, созданный с помощью Flask и DialoGPT на Python.

## Запуск

- Установите зависимости `pip install -r requirements.txt`
- Запустите приложение `python main.py`
- Перейдите в браузере по адресу http://localhost:5000
- Начните чат с ботом в интерфейсе

## Как это работает
- Используется Flask для создания веб приложения
- С помощью DialoGPT генерируются ответы на вопросы пользователя
- Модель и токенизатор загружаются из pretrained моделей transformers
- Текст пользователя обрабатывается и подается на вход модели
- Модель генерирует ответ, который возвращается через Flask

## Используемые библиотеки
![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)
![Torch](https://img.shields.io/badge/Torch-%23EE4C2C.svg?style=for-the-badge&logo=PyTorch&logoColor=white)	
![TensorFlow](https://img.shields.io/badge/TensorFlow-%23FF6F00.svg?style=for-the-badge&logo=TensorFlow&logoColor=white)

## Файлы
- `app.py`- основной код приложения Flask
- `templates/chatbot.html`- шаблон интерфейса чат-бота
- `requirements.txt`- зависимости
- `static/style.css`- стили для интерфейса чат-бота
