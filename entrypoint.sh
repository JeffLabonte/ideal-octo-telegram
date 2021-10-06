#!/bin/bash
echo "Waiting 15 seconds - Give time to PGSQL to build up"
sleep 15
cd /opt/code && ./manage.py makemigrations --settings=settings.prod && ./manage.py migrate --settings=settings.prod && gunicorn settings.wsgi
