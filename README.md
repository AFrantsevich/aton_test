<h2>Всем привет, это Андрей <img src="https://github.com/blackcater/blackcater/raw/main/images/Hi.gif" height="32"/></h2>
</h2> 

<h3>Вы находитесь на странице моего проекта по тестовому заданию Aton</h3> 

### Суть задания:

#### Таблица клиентов:

- Номер счета
- Фамилия
- Имя
- Отчество
- Дата рождения
- ИНН
- ФИО ответственного
- Статус (по умолчанию «Не в работе»)


#### Таблица пользователей:
- ФИО
- Логин
- Пароль


### Создать интерфейс для обращения к синтезированным данным:
Форма для авторизации по паре логин/пароль. 
После показать таблицу клиентов авторизованного
пользователя по связи ФИО из таблицы пользователей – ФИО
ответственного.
Пользователь должен иметь возможность изменить статус
клиента на «В работе», «Отказ», «Сделка закрыта».

P.S. Сотрудники связаны с клиентам M2M из предположения, что
у клиента может быть несколько ответвенных. Управление
данными производится в админке.

## Технологии:

<details><summary>Подробнее</summary>

**Языки программирования и модули:**

[![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)](https://www.python.org/)


**Фреймворк, расширения и библиотеки:**

[![Django](https://img.shields.io/badge/Django-v5.0.2-blue?logo=Django)](https://www.djangoproject.com/)


**Базы данных и инструменты работы с БД:**

[![SQLite3](https://img.shields.io/badge/-SQLite3-464646?logo=SQLite)](https://www.sqlite.com/version3.html)
[![PostgreSQL](https://img.shields.io/badge/-PostgreSQL-464646?logo=PostgreSQL)](https://www.postgresql.org/)

**Фронт:**

![Static Badge](https://img.shields.io/badge/Bootstrap-5.2.0-blue?logo=Bootstrap&logoColor=blue)

**CI/CD:**


[![docker_compose](https://img.shields.io/badge/-Docker%20Compose-464646?logo=docker)](https://docs.docker.com/compose/)
[![gunicorn](https://img.shields.io/badge/-gunicorn-464646?logo=gunicorn)](https://gunicorn.org/)
[![Nginx](https://img.shields.io/badge/-NGINX-464646?logo=NGINX)](https://nginx.org/ru/)


</details>

## Запуск:

<details><summary>Подробнее</summary>


В первую очeредь для удосбва тестирования проект запущен на удаленном сервере и доступен по адресу:
`http://78.141.242.95/`

Учетные данные для входа:
````
Username: test
Password: Qwerty123456!
````


Доступ в админ панель:
`http://78.141.242.95/admin/`

Учетные данные для входа:
````
Username: adm
Password: adm
````


<details><summary>Локальный запуск: Docker Compose/PostgreSQL</summary>

1. Клонируйте репозиторий с GitHub:
   ```bash
   git clone git@github.com:AFrantsevich/aton_test.git
   ```
   
2. В корневой директории проекта создайте файл .env для примера в директории находится [.env_example](.env_example). 
В случае отсутсвия данных, оставьте файл пустым. Главное что бы файл физически присутсвовал в директории.


3. Из корневой директории проекта выполните команду:
   ```bash
   docker-compose up -d --build 
   ```
   Проект будет развернут в трех docker-контейнерах (db, web, nginx) по адресу `http://localhost`.


4. В случае проблем наполнение БД. Вручную из корневой директории выполните следующие компанды:
   ```bash
   docker-compose exec web python manage.py migrate && \
   docker-compose exec web python manage.py createsuperuser  && \
   docker-compose exec web python manage.py collectstatic --no-input 
   ```

5. Доступ в админ панель:
   `http://localhost/admin/`
   
   Учетные данные для входа:
   ````
   Username: adm
   Password: adm
   ````

6. Остановить docker и удалить контейнеры можно командой из корневой директории проекта:
   ```bash
   docker compose -f docker-compose.yml down
   ```
   Если также необходимо удалить тома базы данных, статики и медиа:
   ```bash
   docker compose -f docker-compose.yml down -v
   ```
</details>

<details><summary>Локальный запуск: Django/SQLite3</summary>

1. Клонируйте репозиторий с GitHub:
   ```bash
   git clone git@github.com:AFrantsevich/aton_test.git
   ```

2. Создайте и активируйте виртуальное окружение:
   * Если у вас Linux/macOS
   ```bash
    python -m venv venv && source venv/bin/activate
   ```
   * Если у вас Windows
   ```bash
    python -m venv venv && source venv/Scripts/activate
   ```
   
3. Установите в виртуальное окружение все необходимые зависимости из файла **requirements.txt**:
   ```bash
   python -m pip install --upgrade pip && pip install -r requirements.txt
   ```

4. В корневой директории проекта создайте файл .env для примера в директории находится [.env_example](.env_example). 
В случае отсутсвия данных, оставьте файл пустым. Главное что бы файл физически присутсвовал в директории.


5. Примените миграции, наполните БД тестовыми данными, создайте суперюзера, запустите приложение из корневой директории:
   ```bash
   python manage.py migrate && \
   python manage.py create_superuser && \
   python manage.py runserver
   ```
   Сервер запустится локально по адресу `http://127.0.0.1:8000/`


6. Остановить приложение можно комбинацией клавиш Ctl-C.
</details>