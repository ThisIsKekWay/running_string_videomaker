#!/bin/bash

python manage.py makemigrations

pyhton manage.py migrate

python manage.py runserver 0.0.0.0:8000