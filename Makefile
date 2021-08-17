install:
	pip install -e .['dev']

# init_db:
# 	FLASK_APP=wallet/app.py flask create-db
# 	FLASK_APP=wallet/app.py flask db upgrade

run-dev:
	FLASK_APP=wallet/app.py FLASK_ENV=development flask run

run:
	FLASK_APP=wallet/app.py FLASK_ENV=production flask run

create-db:
	FLASK_APP=wallet/app.py flask create-db

list-db:
	FLASK_APP=wallet/app.py flask list-db

create-fake-data:
	FLASK_APP=wallet/app.py flask add-gains -de="data fake" -am=5.2