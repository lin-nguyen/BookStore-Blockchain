Set up work environment:
- Python: Install Python 3.6.4 
- IDE: Install Pycharm / VS Code
- Django: Install django version 2.0.7
- venv
- python3 -m venv testenv
- source testenv/bin/activate
- pip install required libraries / packages
- Database: Install Postgres, create database has name 'BookStore', the owner is 'postgres' and password is 'fromBKU2017'
- python manage.py flush # to clear old database
- python manage.py migrate # to create tables
- python manage.py createsuperuser # to create admin account
- python manage.py data # insert mock up data
- python manage.py runserver # run local server port 8000

