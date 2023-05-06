#!/bin/sh

tailwindcss -i django_chatgpt/static/css/style.css -o django_chatgpt/static/css/output.css --minify
python manage.py collectstatic --noinput
python manage.py migrate
python manage.py makesuperuser
gunicorn config.wsgi --config="docker/gunicorn.conf.py"
