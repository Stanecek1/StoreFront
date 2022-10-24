release: python manage.py migrate
web: gunicorn firstapp.wsgi
worker: celery-a firstapp worker