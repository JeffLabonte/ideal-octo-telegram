install_dev: venv
	pip install -r requirements.dev.txt

venv:
	python3 -m venv .venv

settings:
	cp src/settings/extra_settings.py.template src/settings/extra_settings.py
