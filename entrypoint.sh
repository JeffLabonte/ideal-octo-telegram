#!/bin/bash
echo "Waiting 5 seconds - Give time to PGSQL to build up"
sleep 5
cd /opt/code && ./manage.py makemigrations --settings=settings.prod && ./manage.py migrate --settings=settings.prod && gunicorn -w 3 -b 0.0.0.0:8000 settings.wsgi
