Приложение управления заказами и АPI  заказов.
Стек
-python 3.11
-isort black mypy. flake8
-django 5.1.7
-SQLite


Requirements:

pip install -r requirements.txt

python manage.py makemigrations

python manage.py migrate

python manage.py runserver
