## 🚀 Система управления взаимоотношениями с клиентами.

Система является полностью open source решением. Использование проекта разрешно в соответствии с условиями лицензии BSD 2 Clause License.

### 📋 Техническое задание проекта:

<a href="https://sogorich.notion.site/sogorich/baf2ac284a5f4b518ed6a2810e8573bc">Открыть ТЗ</a>

### 🎲 Ключевые возможности системы:

1. Система аутентификации в системе;
2. Добавление новых сотрудников в систему (для администраторов);
3. Возможность разделения клиентов на “горячих” и “холодных” (лиды);
4. Отправка сообщений по заявкам на почту клиента;
5. Воронка продаж:
    1. Новые заявки;
    2. Консультация;
    3. Оплата;
    4. Завершение сделки.
6. Страница аналитики. Каждый раздел должен быть доступен для просмотра за последний месяц, квартал, год. Статистика по разделам:
    1. Новые клиенты;
    2. Заработано средств;
    3. Потеряно клиентов;
    4. Успешные сделки.

### 👔 Руководство проекта:

<strong>Lead</strong> <a href="https://github.com/sogorich/">sogorich</a> <br>
<strong>Admin</strong> <a href="https://github.com/vami7ir/">vami7ir</a>

### 📚 Поддержка проекта:

Будем рады если вы Внесёте свой вклад в этот проект или поддержите его материально.

#### На развитие проекта:
- <a href="https://yoomoney.ru/to/410017296852683/50/">Поддержать проект (ЮMoney)</a>

### 👍 Благодарности:

#### Благодарность Ивану за помощь в организации работы проекта:
- <strong>Github</strong> <a href="https://github.com/vami7ir/">vami7ir</a>

#### Благодарность за иллюстрации используемые в дизайне:
- <a href="https://undraw.co/illustrations/">unDraw</a>
- <a href="https://www.pixeltrue.com/free-illustrations/">pixeltrue</a>

#### Благодарность за шрифты и иконки используемые в дизайне:
- <a href="https://fonts.google.com/">Google fonts</a>
- <a href="https://fonts.google.com/icons/">Google icons</a>

### 💡 Руководство по использованию:

#### 1) Клонировать репозиторий;

#### 2) В корне проекта создать файл <b>.env</b> и прописать следующие настройки:
<pre>
# Main options
SECRET_KEY=django-insecure-hxo3nui5a-*g!bhqqke@5hw58s1&e2pc_0b@05d6xcvwm#bc=&
DEBUG=True
ALLOWED_HOSTS=127.0.0.1 localhost

# Other options
LANGUAGE_CODE=ru
TIME_ZONE=Europe/Moscow

# Postgres options
POSTGRES_ENGINE=django.db.backends.postgresql
POSTGRES_HOST=db
POSTGRES_PORT=5432

POSTGRES_DB=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres

# CORS tech options
CORS_ALLOWED_ORIGINS=http://localhost:8000 http://127.0.0.1:8000

# REST FRAMEWORK option
REST_RENDERER=rest_framework.renderers.JSONRenderer rest_framework.renderers.BrowsableAPIRenderer
</pre>

#### 3) Выполнить команду:
<pre>
docker-compose up --build
</pre>

<b>Данная команда создаст нужные образы и обернёт их в контейнеры, после чего запустит.</b>

#### 4) Выполнить команды:
<pre>
docker exec -it crm_backend_1 bash
</pre>
<pre>
python manage.py makemigrations
</pre>
<pre>
python manage.py migrate
</pre>
<pre>
exit
</pre>
<pre>
docker-compose down -v
</pre>
<pre>
docker-compose up
</pre>

