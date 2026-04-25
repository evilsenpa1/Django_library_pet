<div align="center">

# 📚 Library API

**A RESTful API for managing books and authors — built with Django 5 & DRF**

[![Python](https://img.shields.io/badge/Python-3.12-3776AB?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-5.x-092E20?style=flat&logo=django&logoColor=white)](https://www.djangoproject.com/)
[![DRF](https://img.shields.io/badge/DRF-3.15-red?style=flat)](https://www.django-rest-framework.org/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-psycopg3-336791?style=flat&logo=postgresql&logoColor=white)](https://www.postgresql.org/)
[![JWT](https://img.shields.io/badge/Auth-JWT-000000?style=flat&logo=jsonwebtokens&logoColor=white)](https://github.com/jazzband/djangorestframework-simplejwt)
[![Ruff](https://img.shields.io/badge/linter-ruff-D7FF64?style=flat)](https://docs.astral.sh/ruff/)

---

*[English](#english) · [Українська](#ukrainian)*

</div>

---

<a name="english"></a>

## 🇬🇧 English

### Overview

Library API is a pet project — a backend REST API for a library catalog. It supports managing books, authors, and users with JWT authentication, file uploads, and interactive Swagger documentation out of the box.

### Features

- **Books** — create, read, update, delete books with file attachments (PDFs, etc.)
- **Authors** — manage authors with a Many-to-Many relationship to books
- **Users** — registration and profile management
- **JWT Authentication** — access & refresh token flow via `simplejwt`
- **Swagger UI** — interactive API docs at `/api/docs/`
- **Pagination** — page-based, 20 items per page
- **CORS** — configured via `django-cors-headers`
- **Environment-based config** — all secrets live in `.env`, never in code

### Tech Stack

| Layer | Technology |
|---|---|
| Framework | Django 5, Django REST Framework 3.15 |
| Database | PostgreSQL (psycopg3) |
| Auth | JWT via `djangorestframework-simplejwt` |
| Docs | OpenAPI 3.0 via `drf-spectacular` (Swagger UI + ReDoc) |
| Config | `django-environ` |
| CORS | `django-cors-headers` |
| Linter | `ruff` (E, F, W, B, UP, DJ, RUF rules) |

### Project Structure

```
app/                  ← Django project config (settings, urls, wsgi)
books/                ← Books app (model, serializer, viewset, admin)
authors/              ← Authors app (model, serializer, viewset, admin)
users/                ← Users app (serializer, viewset — uses built-in auth.User)
media/                ← Uploaded files (gitignored)
```

### Data Model

```
BookModel
├── name         CharField(255)
├── description  CharField(1000)
├── date         DateField          ← publication / release date
├── pub_date     DateTimeField      ← auto-set on creation
└── book_file    FileField          ← uploaded to media/%Y/%m/%d/

AuthorModel
├── name           CharField(255)
├── date_of_birth  DateField
├── pub_date       DateTimeField    ← auto-set on creation
└── books          ManyToManyField → BookModel   (reverse: book.authors)
```

### API Endpoints

| Method | Endpoint | Auth required | Description |
|---|---|---|---|
| `POST` | `/api/v1/token/` | No | Obtain JWT access + refresh tokens |
| `POST` | `/api/v1/token/refresh/` | No | Refresh access token |
| `GET` | `/api/v1/books/` | No | List all books (paginated) |
| `POST` | `/api/v1/books/` | Yes | Create a book |
| `GET` | `/api/v1/books/{id}/` | No | Retrieve a book |
| `PUT/PATCH` | `/api/v1/books/{id}/` | Yes | Update a book |
| `DELETE` | `/api/v1/books/{id}/` | Yes | Delete a book |
| `GET` | `/api/v1/authors/` | No | List all authors (paginated) |
| `POST` | `/api/v1/authors/` | Yes | Create an author |
| `GET` | `/api/v1/authors/{id}/` | No | Retrieve an author |
| `PUT/PATCH` | `/api/v1/authors/{id}/` | Yes | Update an author |
| `DELETE` | `/api/v1/authors/{id}/` | Yes | Delete an author |
| `POST` | `/api/v1/users/` | No | Register a new user |
| `GET` | `/api/v1/users/{id}/` | Yes | Get user profile |
| `PUT/PATCH` | `/api/v1/users/{id}/` | Yes | Update profile / change password |
| `GET` | `/api/docs/` | — | Swagger UI |
| `GET` | `/api/schema/` | — | Raw OpenAPI schema (JSON/YAML) |

### Getting Started

#### 1. Clone the repository

```bash
git clone https://github.com/evilsenpa1/Django_library_pet.git
cd Django_library_pet
```

#### 2. Create and activate a virtual environment

```bash
python -m venv .venv

# Linux / macOS
source .venv/bin/activate

# Windows
.venv\Scripts\activate
```

#### 3. Install dependencies

```bash
pip install -r requirements.txt
```

#### 4. Configure environment variables

Copy the example and fill in your values:

```bash
cp .env.example .env
```

`.env` variables:

```ini
SECRET_KEY=your-secret-key-here
DEBUG=True
DATABASE_URL=postgres://user:password@localhost:5432/library_db
ALLOWED_HOSTS=localhost,127.0.0.1
LANGUAGE_CODE=en-us
TIME_ZONE=UTC
```

#### 5. Apply migrations

```bash
python manage.py migrate
```

#### 6. Create a superuser (optional)

```bash
python manage.py createsuperuser
```

#### 7. Run the development server

```bash
python manage.py runserver
```

API is available at `http://127.0.0.1:8000/`
Swagger UI at `http://127.0.0.1:8000/api/docs/`

### Running Tests

```bash
# All tests
python manage.py test

# Per app
python manage.py test books
python manage.py test authors
python manage.py test users
```

### Linting & Formatting

```bash
# Check
ruff check .

# Auto-fix
ruff check --fix .

# Format
ruff format .
```

---

<a name="ukrainian"></a>

## 🇺🇦 Українська

### Огляд

Library API — пет-проєкт, бекенд REST API для бібліотечного каталогу. Підтримує управління книгами, авторами та користувачами з JWT-автентифікацією, завантаженням файлів та інтерактивною Swagger-документацією.

### Функціональність

- **Книги** — CRUD із прикріпленням файлів (PDF тощо)
- **Автори** — управління авторами зі зв'язком Many-to-Many до книг
- **Користувачі** — реєстрація та управління профілем
- **JWT-автентифікація** — flow access + refresh токенів через `simplejwt`
- **Swagger UI** — інтерактивна документація API за адресою `/api/docs/`
- **Пагінація** — посторінкова, 20 елементів на сторінку
- **CORS** — налаштований через `django-cors-headers`
- **Конфігурація через env** — усі секрети у `.env`, ніколи в коді

### Технологічний стек

| Шар | Технологія |
|---|---|
| Фреймворк | Django 5, Django REST Framework 3.15 |
| База даних | PostgreSQL (psycopg3) |
| Автентифікація | JWT через `djangorestframework-simplejwt` |
| Документація | OpenAPI 3.0 через `drf-spectacular` (Swagger UI + ReDoc) |
| Конфігурація | `django-environ` |
| CORS | `django-cors-headers` |
| Лінтер | `ruff` (правила E, F, W, B, UP, DJ, RUF) |

### Структура проєкту

```
app/                  ← Конфіг Django-проєкту (settings, urls, wsgi)
books/                ← Застосунок книг (модель, серіалізатор, viewset, admin)
authors/              ← Застосунок авторів (модель, серіалізатор, viewset, admin)
users/                ← Застосунок користувачів (використовує вбудований auth.User)
media/                ← Завантажені файли (gitignored)
```

### Модель даних

```
BookModel
├── name         CharField(255)
├── description  CharField(1000)
├── date         DateField          ← дата публікації / виходу
├── pub_date     DateTimeField      ← встановлюється автоматично при створенні
└── book_file    FileField          ← завантажується у media/%Y/%m/%d/

AuthorModel
├── name           CharField(255)
├── date_of_birth  DateField
├── pub_date       DateTimeField    ← встановлюється автоматично при створенні
└── books          ManyToManyField → BookModel   (reverse: book.authors)
```

### API ендпоінти

| Метод | Ендпоінт | Авторизація | Опис |
|---|---|---|---|
| `POST` | `/api/v1/token/` | Ні | Отримати JWT access + refresh токени |
| `POST` | `/api/v1/token/refresh/` | Ні | Оновити access токен |
| `GET` | `/api/v1/books/` | Ні | Список книг (пагінація) |
| `POST` | `/api/v1/books/` | Так | Створити книгу |
| `GET` | `/api/v1/books/{id}/` | Ні | Отримати книгу |
| `PUT/PATCH` | `/api/v1/books/{id}/` | Так | Оновити книгу |
| `DELETE` | `/api/v1/books/{id}/` | Так | Видалити книгу |
| `GET` | `/api/v1/authors/` | Ні | Список авторів (пагінація) |
| `POST` | `/api/v1/authors/` | Так | Створити автора |
| `GET` | `/api/v1/authors/{id}/` | Ні | Отримати автора |
| `PUT/PATCH` | `/api/v1/authors/{id}/` | Так | Оновити автора |
| `DELETE` | `/api/v1/authors/{id}/` | Так | Видалити автора |
| `POST` | `/api/v1/users/` | Ні | Зареєструвати користувача |
| `GET` | `/api/v1/users/{id}/` | Так | Отримати профіль |
| `PUT/PATCH` | `/api/v1/users/{id}/` | Так | Оновити профіль / змінити пароль |
| `GET` | `/api/docs/` | — | Swagger UI |
| `GET` | `/api/schema/` | — | OpenAPI схема (JSON/YAML) |

### Початок роботи

#### 1. Клонування репозиторію

```bash
git clone https://github.com/evilsenpa1/Django_library_pet.git
cd Django_library_pet
```

#### 2. Створення та активація віртуального середовища

```bash
python -m venv .venv

# Linux / macOS
source .venv/bin/activate

# Windows
.venv\Scripts\activate
```

#### 3. Встановлення залежностей

```bash
pip install -r requirements.txt
```

#### 4. Налаштування змінних оточення

Скопіюй приклад і заповни своїми значеннями:

```bash
cp .env.example .env
```

Змінні `.env`:

```ini
SECRET_KEY=твій-секретний-ключ
DEBUG=True
DATABASE_URL=postgres://user:password@localhost:5432/library_db
ALLOWED_HOSTS=localhost,127.0.0.1
LANGUAGE_CODE=uk
TIME_ZONE=Europe/Kyiv
```

#### 5. Застосування міграцій

```bash
python manage.py migrate
```

#### 6. Створення суперкористувача (опціонально)

```bash
python manage.py createsuperuser
```

#### 7. Запуск сервера розробки

```bash
python manage.py runserver
```

API доступне за адресою `http://127.0.0.1:8000/`
Swagger UI за адресою `http://127.0.0.1:8000/api/docs/`

### Запуск тестів

```bash
# Усі тести
python manage.py test

# По застосунку
python manage.py test books
python manage.py test authors
python manage.py test users
```

### Лінтинг та форматування

```bash
# Перевірка
ruff check .

# Авто-виправлення
ruff check --fix .

# Форматування
ruff format .
```

---

<div align="center">

Made with ☕ and Python

</div>
