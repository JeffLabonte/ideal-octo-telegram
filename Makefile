SHELL = '/bin/bash'

WORKDIR_DIRECTORY = 'src'

install:
	poetry install

runserver: install
	cd ${WORKDIR_DIRECTORY} && poetry run python3 manage.py runserver 0.0.0.0:8000

makemigrations:
	cd ${WORKDIR_DIRECTORY} && poetry run python3 manage.py makemigrations

migrate: install makemigrations
	cd ${WORKDIR_DIRECTORY} && poetry run python3 manage.py migrate

test_integration:
	cd ${WORKDIR_DIRECTORY} && poetry run py.test --cov=../src --cov-report term --cov-report xml --testdox --ds=settings.test tests

build_container:
	docker build -t grimsleepless/ideal-octo-telegram . && docker push grimsleepless/ideal-octo-telegram

copy_new_config:
	@if [ -f "deploy/hosts.yml" ]; then \
		cp deploy/hosts.yml deploy/hosts.yml.back; \
	fi
	cp deploy/hosts.yml.example deploy/hosts.yml
