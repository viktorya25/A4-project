# Инструкции для работы с проектом A4

## Как запустить проект

1) Склонировать проект:
```bash
git clone https://github.com/SSerov77/A4-django.git
```

2) Перейти в склоннированную папку проекта:
```bash
cd A4-django
```

3) Создать папку с виртуальным окружением:
```bash
python -m venv venv
```

4) Активировать виртуальное окружение <i>(советую в cmd, тк по умолчанию в VSCode создается терминал Powershell)</i>
```bash
venv\Scripts\activate
```

5) Установить необходимые библиотеки:
```bash
pip install -r requirements.txt
```

6) Перейти в папку с приложением:
```bash
cd a4
```

7) Запустить файл запуска:
```bash
python manage.py runserver
```
> Пример запуска:<br>
[![image.png](https://i.postimg.cc/rpBzycdj/image.png)](https://postimg.cc/06C9ZT0K)

6) Перейти в браузере по ссылке:
```bash
http://127.0.0.1:8000/
```


## Как создать базу данных

1) Создать миграции: 
```bash
python manage.py makemigrations
```
> Пример:<br>
[![image.png](https://i.postimg.cc/SKT7gnvs/image.png)](https://postimg.cc/8Fv65zDQ)

2) Применить миграции:
```bash
python manage.py migrate
```
> Пример:<br>
[![image.png](https://i.postimg.cc/NfkXNyyc/image.png)](https://postimg.cc/PPNNJ5z3)


## Как создать Администратора

1) Создать суперпользователя:
```bash
python manage.py createsuperuser
```

2) Заполнить данные аккаунта, пример:
[![image.png](https://i.postimg.cc/R0VL17Gy/image.png)](https://postimg.cc/4YqcshDQ)

3) Чтобы перейти на Панель Администратора нужно перейти по ссылке:
```bash
http://127.0.0.1:8000/admin
```

## Обновление на сервере

1) Зайти через терминал на сервер:
```bash
ssh root@109.73.194.27
```

2) Ввести пароль:
```bash
cs18Fx2Z+5PMrv
```
> **Важно:** В терминале пароль не отображается. Просто копируешь пароль, нажимаешь в терминале ПКМ и он вставляется. Затем Enter.

3) Перейти в папку проекта:
```bash
cd A4-django
```

4) Склонировать изменения:
```bash
git pull
```

5) Перезапустить Docker контейнер:
```bash
docker-compose up --build -d
```