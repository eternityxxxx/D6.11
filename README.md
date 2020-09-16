# D6.11
Module D6 homework


#### Как развернуть проект:
1. Создаем новый каталог виртуального окружения:
```
    python -m venv <Имя каталога>
```
2. Стянуть репозиторий к себе:
```
    git clone https://github.com/eternityxxxx/D5.11.git
```
3. Активируем виртуальное окружения:
```
    <Имя каталога>/Scripts/activate
```
4. Установить зависимости из requirements.txt:
```
    pip install -r requirements.txt
```
5. При создании файла с фикстурой возникли проблемы с кодировкой, поэтому:
###### Сразу запускаем сервер с клонированной из репозитория БД
```
    cd 'my_library'
    python manage.py runserver
```
###### Или удаляем файлы миграций <p_library/migrations> и файл с БД <db.sqlite3>. Проводим миграции:
```
    python manage.py makemigrations
    python manage.py migrate
```
###### И создаем супер пользователя для внесения собственных данных
```
    pythyon manage.py createsuperuser
```
