#!/bin/bash

set -e

# make migrations on code to run as less previleged user in container
# python manage.py makemigrations

python manage.py migrate

python manage.py collectstatic --no-input

gunicorn -c gunicorn.conf.py