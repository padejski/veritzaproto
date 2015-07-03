web: gunicorn wsgi:application --log-file - & python manage.py scrape
# web: scrapyd
#scheduler: python manage.py celery worker -B -E --maxtasksperchild=1000
#worker: python manage.py celery worker -E --maxtasksperchild=1000
