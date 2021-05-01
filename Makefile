install_dev: venv
	pip install -r requirements.dev.txt

venv:
	python3 -m venv .venv
