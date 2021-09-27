SHELL = '/bin/bash'

WORKDIR_DIRECTORY = 'src'

install:
	poetry install

runserver: install
	cd ${WORKDIR_DIRECTORY} && poetry run python3 manage.py runserver 0.0.0.0:8000

migrate: install
	cd ${WORKDIR_DIRECTORY} && poetry run python3 manage.py migrate


