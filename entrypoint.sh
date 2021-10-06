#!/bin/bash
echo "Waiting 30 seconds - Give time to PGSQL to build up"
sleep 30
cd /opt/code && ./manage.py migrate --settings=settings.prod 
