<div id="top">

<!-- HEADER STYLE: CLASSIC -->
<div align="center">


# DDS-TEST-TASK

<em>Empowering Seamless Cashflow Management at Scale</em>

<!-- BADGES -->
<img src="https://img.shields.io/github/last-commit/ove4lo/dds-test-task?style=flat&logo=git&logoColor=white&color=0080ff" alt="last-commit">
<img src="https://img.shields.io/github/languages/top/ove4lo/dds-test-task?style=flat&color=0080ff" alt="repo-top-language">
<img src="https://img.shields.io/github/languages/count/ove4lo/dds-test-task?style=flat&color=0080ff" alt="repo-language-count">

<em>Built with the tools and technologies:</em>

<img src="https://img.shields.io/badge/Markdown-000000.svg?style=flat&logo=Markdown&logoColor=white" alt="Markdown">
<img src="https://img.shields.io/badge/Docker-2496ED.svg?style=flat&logo=Docker&logoColor=white" alt="Docker">
<img src="https://img.shields.io/badge/Python-3776AB.svg?style=flat&logo=Python&logoColor=white" alt="Python">

</div>
<br>

---

## Оглавление

- [Обзор](#обзор)
- [Начало работы](#начало-работы)
    - [Предварительные требования](#предварительные-требования)
    - [Установка](#установка)
    - [Использование](#использование)
  
---

## Веб-сервис для управления движением денежных средств (ДДС)

Этот проект представляет собой веб-сервис для учёта и управления денежными операциями. Приложение позволяет пользователям создавать, редактировать, удалять и просматривать записи о движении денежных средств с учётом логических зависимостей между сущностями.

**Основные возможности:**

- 📊 Управление финансовыми записями (доходы/расходы)
- 🗂️ Иерархическая система категорий
- 📝 Типы записей с настраиваемыми статусами
- 📚 Документированный API через Swagger (/swagger/)
- 🛠️ Админ-панель Django для управления данными
- 🐳 Готовая Docker-конфигурация для быстрого развертывания

**Доступные интерфейсы:**
- Swagger UI: `http://localhost/swagger/`
- Admin Panel: `http://localhost/admin/` (требуется создать суперпользователя)

---

## Начало работы

### Предварительные требования

- Python 3.9+
- Docker
- Pip

### Установка

1. **Клонируйте репозиторий:**

    ```sh
    ❯ git clone https://github.com/ove4lo/dds-test-task
    ```

2. **Перейдите в директорию проекта:**

    ```sh
    ❯ cd dds-test-task
    ```

3.  **Установите зависимости:**

**Используйте [docker](https://www.docker.com/):**

```sh
❯ docker build -t ove4lo/dds-test-task .
```
**Используйте [pip](https://pypi.org/project/pip/):**

```sh
❯ pip install -r requirements.txt
```

### Использование

Для запуска понадобится:

**Используйте [docker](https://www.docker.com/):**

```sh
docker run -it {image_name}
```
**Используйте [pip](https://pypi.org/project/pip/):**

```sh
python {entrypoint}
```

---

<div align="left"><a href="#top">⬆ Вернуться</a></div>

---
