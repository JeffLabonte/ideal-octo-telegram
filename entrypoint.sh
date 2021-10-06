#!/bin/bash


cd /opt/code && ./manage.py migrate --settings=settings.prod 
