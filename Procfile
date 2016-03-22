web: gunicorn config.wsgi:application
worker: celery worker --app=bogg.taskapp --loglevel=info
