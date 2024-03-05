install:
	poetry install

lint:
	poetry run flake8 rooky_teams

dev-server:
	poetry run python3 manage.py runserver

PORT ?= 8000
prod-server:
	poetry run gunicorn -w 5 -b 0.0.0.0:$(PORT) rooky_teams.wsgi

migrate:
	poetry run python3 manage.py makemigrations
	poetry run python3 manage.py migrate

test:
	poetry run python3 manage.py test

coverage:
	poetry run python3 -m coverage run manage.py test

cov-report:
	poetry run python3 -m coverage xml

selfcheck:
	poetry check

check: selfcheck test lint

shell:
	poetry run python3 manage.py shell

loc-upd:
	django-admin makemessages -l ru

loc-com:
	django-admin compilemessages

deploy: install migrate