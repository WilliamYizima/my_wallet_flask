install:
	pip install -e .['dev']

init_db:
	FLASK_APP=wallet/app.py flask create-db
	FLASK_APP=wallet/app.py flask db upgrade

run-dev:
	FLASK_APP=wallet/app.py FLASK_ENV=development flask run