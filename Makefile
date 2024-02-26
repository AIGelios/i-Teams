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