install:
	poetry install

lint:
	poetry run flake8 rooky_teams

dev-server:
	poetry run python3 manage.py runserver

migrate:
	poetry run python3 manage.py makemigrations
	poetry run python3 manage.py migrate

test:
	poetry run python3 manage.py test

coverage:
	poetry run coverage run --source='.' manage.py test
	poetry run coverage xml

selfcheck:
	poetry check

check: selfcheck test lint