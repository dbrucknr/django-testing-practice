# First Time Running the Server:

1. `source env/bin/activate`
2. `pip install -r requirements.txt`
3. `python src/manage.py runserver`

# To run tests:

- input `pytest` into terminal from main directory (README, env, src, requirements.txt all visible)

# Project Creation Steps:

1. python --version
2. python -m venv env
3. source env/bin/activate
4. pip freeze > requirements.txt
5. pip install django
6. pip freeze > requirements.txt
7. pip install pytest
8. pip freeze > requirements.txt
9. pytest --version
10. mkdir src && cd src
11. django-admin startproject api .
12. python manage.py startapp accounts
13. python manage.py makemigrations
14. python manage.py migrate
15. python manage.py createsuperuser
