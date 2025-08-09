# DDS-TEST-TASK

*Веб-сервис для управления движением денежных средств (ДДС)*

![last-commit](https://img.shields.io/github/last-commit/ove4lo/dds-test-task?style=flat&logo=git&logoColor=white&color=0080ff)
![repo-top-language](https://img.shields.io/github/languages/top/ove4lo/dds-test-task?style=flat&color=0080ff)
![repo-language-count](https://img.shields.io/github/languages/count/ove4lo/dds-test-task?style=flat&color=0080ff)

*Создано с использованием следующих технологий:*

![Markdown](https://img.shields.io/badge/Markdown-000000.svg?style=flat&logo=Markdown&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED.svg?style=flat&logo=Docker&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB.svg?style=flat&logo=Python&logoColor=white)
![Django](https://img.shields.io/badge/Django-092E20.svg?style=flat&logo=Django&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1.svg?style=flat&logo=PostgreSQL&logoColor=white)

---

## Содержание

- [Обзор](#overview)
- [Возможности](#features)
- [Начало работы](#getting-started)
  - [Предварительные требования](#prerequisites)
  - [Установка](#installation)
  - [Инициализация базы данных](#database-initialization)
  - [Использование](#usage)
- [API Эндпоинты](#api-endpoints)
- [Интерфейсы](#interfaces)
---

## Обзор <a name="overview"></a>

**DDS-TEST-TASK** — это веб-сервис, разработанный на фреймворке Django, предназначенный для учёта и управления движением денежных средств. Проект предоставляет удобный инструментарий для создания, редактирования, удаления и просмотра финансовых записей с учётом логических зависимостей между сущностями. Использует PostgreSQL в качестве базы данных, Django Admin Panel с библиотекой Unfold для улучшенного интерфейса администрирования и Swagger для документирования API.

Сервис поддерживает управление категориями, типами записей, статусами и финансовыми записями через RESTful API и интуитивно понятный интерфейс администратора.

![Скриншот главного экрана](https://github.com/ove4lo/dds-test-task/blob/main/images/main.png)

---

## Возможности <a name="features"></a>

- 📊 **Управление финансовыми записями:** Создание, редактирование и удаление записей о доходах и расходах.
- 🗂️ **Иерархическая система категорий:** Поддержка вложенных категорий для структурирования финансовых данных.
- 📝 **Типы записей и статусы:** Настраиваемые типы записей и их статусы для гибкой классификации.
- 📚 **Документированный API:** Полная документация API доступна через Swagger UI (`/swagger/`).
- 🛠️ **Админ-панель:** Улучшенная Django Admin Panel с использованием библиотеки Unfold для удобного управления данными.
- 🐳 **Контейнеризация:** Docker и Docker Compose для быстрого развертывания и一эного окружения.
- 🚀 **Гибкое развертывание:** Поддержка асинхронного (ASGI) и синхронного (WSGI) режимов для продакшн-сред.

---

## Начало работы <a name="getting-started"></a>

### Предварительные требования <a name="prerequisites"></a>

Для работы с проектом необходимо установить следующие компоненты:

- **Docker Desktop**: Платформа для управления контейнерами. Убедитесь, что Docker Desktop установлен и работает на вашей системе. [Скачать Docker Desktop](https://www.docker.com/products/docker-desktop/).
- **Git**: Для клонирования репозитория.

Зависимости контейнера (такие как Python, PostgreSQL, и необходимые библиотеки) автоматически устанавливаются при сборке Docker-образа, поэтому дополнительных установок на хост-машине не требуется.

### Установка <a name="installation"></a>

1. **Клонируйте репозиторий:**

    ```sh
    ❯ git clone https://github.com/ove4lo/dds-test-task
    ```

2. **Перейдите в директорию проекта:**

    ```sh
    ❯ cd dds-test-task
    ```

3. **Создайте файл `.env` для переменных окружения:**

   Создайте файл `.env` в корне проекта со следующим содержимым:

   ```env
      POSTGRES_DB=dds_db
      POSTGRES_USER=dds_user
      POSTGRES_HOST=db
      POSTGRES_PASSWORD=ddscashfl0w
      SECRET_KEY=hfzse_*@qo097n-damj*p%5@p+^d=jlv#e2bk%r_-f1l*yw71_
      DEBUG=True
   ```

   Можете заменить `SECRET_KEY` на безопасный ключ (например, сгенерируйте его с помощью `python -c "import secrets; print(secrets.token_hex(32))"`).

4. **Соберите и запустите Docker-контейнеры:**

   ```sh
   ❯ docker-compose up --build
   ```

   Эта команда:
   - Соберет Docker-образ для веб-приложения.
   - Запустит контейнеры для PostgreSQL и веб-приложения.
   - Выполнит миграции базы данных.
   - Инициализирует базу данных тестовыми данными и создаст суперпользователя.

### Инициализация базы данных <a name="database-initialization"></a>

После запуска контейнеров автоматически выполняется скрипт `init_db.py`, который:

- Создает тестовые данные для записей, статусов, типов записей, категорий и подкатегорий согласно спецификации из задания:
  - **Статусы**: Бизнес, Личное, Налог.
  - **Типы**: Пополнение, Списание.
  - **Категории и подкатегории**: Инфраструктура (VPS, Proxy), Маркетинг (Farpost, Avito).
  - **Записи**: Рандомно на основе других классов.
- Создает суперпользователя с учетными данными:
  - **Логин**: `admin`
  - **Пароль**: `admin123`
  - **Email**: `admin@example.com`

Вы можете использовать эти учетные данные для входа в админ-панель.

### Использование <a name="usage"></a>

После выполнения `docker-compose up --build` проект будет доступен по следующим адресам:

- **Swagger UI**: Документация API доступна по адресу `http://localhost:8000/swagger/`.
- **Admin Panel**: Панель администратора доступна по адресу `http://localhost:8000/admin/`. Используйте учетные данные суперпользователя (`admin`/`admin123`).

Для остановки контейнеров используйте:

```sh
❯ docker-compose down
```

## API Эндпоинты <a name="api-endpoints"></a>

RESTful API предоставляет следующие эндпоинты для работы с данными:

### Категории (Categories)

| Метод | Эндпоинт                        | Название действия            | Описание                                      |
|-------|---------------------------------|-----------------------------|-----------------------------------------------|
| GET   | `/categories/`                  | `categories_list`           | Получить список всех категорий                |
| POST  | `/categories/`                  | `categories_create`         | Создать новую категорию                      |
| GET   | `/categories/{id}/`             | `categories_read`           | Получить данные категории по ID              |
| PUT   | `/categories/{id}/`             | `categories_update`         | Полное обновление категории по ID            |
| PATCH | `/categories/{id}/`             | `categories_partial_update` | Частичное обновление категории по ID         |
| DELETE| `/categories/{id}/`             | `categories_delete`         | Удалить категорию по ID                      |
| GET   | `/categories/{id}/by-type/`     | `categories_by_type`        | Получить категории по типу                   |
| GET   | `/categories/{id}/subcategories/` | `categories_subcategories` | Получить подкатегории для категории по ID    |

### Типы записей (Record Types)

| Метод | Эндпоинт                        | Название действия            | Описание                                      |
|-------|---------------------------------|-----------------------------|-----------------------------------------------|
| GET   | `/record-types/`                | `record-types_list`         | Получить список всех типов записей           |
| POST  | `/record-types/`                | `record-types_create`       | Создать новый тип записи                     |
| GET   | `/record-types/{id}/`           | `record-types_read`         | Получить данные типа записи по ID            |
| PUT   | `/record-types/{id}/`           | `record-types_update`       | Полное обновление типа записи по ID          |
| PATCH | `/record-types/{id}/`           | `record-types_partial_update`| Частичное обновление типа записи по ID      |
| DELETE| `/record-types/{id}/`           | `record-types_delete`       | Удалить тип записи по ID                     |

### Записи (Records)

| Метод | Эндпоинт                        | Название действия            | Описание                                      |
|-------|---------------------------------|-----------------------------|-----------------------------------------------|
| GET   | `/records/`                     | `records_list`              | Получить список всех записей                 |
| POST  | `/records/`                     | `records_create`            | Создать новую запись                         |
| GET   | `/records/{id}/`                | `records_read`              | Получить данные записи по ID                 |
| PUT   | `/records/{id}/`                | `records_update`            | Полное обновление записи по ID               |
| PATCH | `/records/{id}/`                | `records_partial_update`    | Частичное обновление записи по ID            |
| DELETE| `/records/{id}/`                | `records_delete`            | Удалить запись по ID                         |

### Статусы (Statuses)

| Метод | Эндпоинт                        | Название действия            | Описание                                      |
|-------|---------------------------------|-----------------------------|-----------------------------------------------|
| GET   | `/statuses/`                    | `statuses_list`             | Получить список всех статусов                |
| POST  | `/statuses/`                    | `statuses_create`           | Создать новый статус                         |
| GET   | `/statuses/{id}/`               | `statuses_read`             | Получить данные статуса по ID                |
| PUT   | `/statuses/{id}/`               | `statuses_update`           | Полное обновление статуса по ID              |
| PATCH | `/statuses/{id}/`               | `statuses_partial_update`   | Частичное обновление статуса по ID           |
| DELETE| `/statuses/{id}/`               | `statuses_delete`           | Удалить статус по ID                         |

---

## Интерфейсы <a name="interfaces"></a>

- **Swagger UI**: Доступ к документации API по адресу `http://localhost:8000/swagger/`. Позволяет тестировать эндпоинты и просматривать их описание.
  ![Скриншот сваггера](https://github.com/ove4lo/dds-test-task/blob/main/images/swagger.png)
- **Django Admin Panel**: Улучшенная админ-панель с использованием библиотеки Unfold, доступная по адресу `http://localhost:8000/admin/`. Используйте учетные данные суперпользователя (`admin`/`admin123`) для входа.

    Скриншот добавления записи:
    ![Скриншот добавления записи](https://github.com/ove4lo/dds-test-task/blob/main/images/add.png)
    Скриншот таблицы с категориями, типами, подкатегориями:
    ![Скриншот таблицы](https://github.com/ove4lo/dds-test-task/blob/main/images/cat.png)


[⬆ Вернуться к началу](#top)
