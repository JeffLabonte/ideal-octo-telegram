#!/bin/bash

cd /opt/code && poetry run manage.py migrate --settings=settings.prod
