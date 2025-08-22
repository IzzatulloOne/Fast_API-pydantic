📚 FastAPI Library API

Этот проект — простой учебный REST API для работы с жанрами, авторами и книгами.
Реализован на FastAPI и Pydantic. Данные хранятся в памяти (без базы данных).

🚀 Возможности

1. Добавление жанров, авторов и книг через POST запросы

2. Получение списка всех жанров, авторов и книг (GET)

3. Получение полного «снимка библиотеки» (жанры + авторы + книги)

4. Валидация входных данных с помощью Pydantic

🛠 Установка и запуск

1. Клонируем репозиторий:
```
git clone https://github.com/your-username/fastapi-library.git
cd fastapi-library
```

2. Создаем виртуальное окружение и активируем его:
```
python -m venv venv
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate
```

3. Устанавливаем зависимости:
```
pip install fastapi uvicorn pydantic
```

4. Запускаем сервер:
```
python main.py
```

API будет доступен по адресу:
👉 http://127.0.0.1:8000
1. Swagger UI: http://127.0.0.1:8000/docs
2. ReDoc: http://127.0.0.1:8000/redoc


📌 Примеры запросов

1. Добавить жанр
```
POST /genres
Content-Type: application/json

{
  "id": 1,
  "title": "Фантастика",
  "description": "Космос и будущее",
  "created_at": 2025
}
```
2. Добавить автора
```
POST /authors
Content-Type: application/json

{
  "id": 1,
  "first_name": "Айзек",
  "last_name": "Азимов",
  "bio": "Автор научной фантастики"
}
```

3. Добавить книгу
```
POST /books
Content-Type: application/json

{
  "id": 1,
  "name": "Основание",
  "author": [1],
  "genres": [1],
  "description": "Классика НФ",
  "year": 1951,
  "available": true
}
```

4. Получить всё содержимое библиотеки
```
GET /library_schema/all
```

5. Получить все книги
```
GET /library_schema/books
```

✅ Примечания

Данные хранятся в памяти, после перезапуска сервера всё обнуляется.

Для тестов удобно использовать Swagger UI или Postman.

Если нужен persistent storage, можно подключить базу данных (SQLite, PostgreSQL).
