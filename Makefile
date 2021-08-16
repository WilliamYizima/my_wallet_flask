install:
	pip install -e .['dev']

init_db:
	FLASK_APP=delivery/app.py flask create-db
	FLASK_APP=delivery/app.py flask db upgrade