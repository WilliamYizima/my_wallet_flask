first commit

# Description
API that fetches bitcoin and chainlink historical data(web-service - mercado Bitcoin)

In the future it will be integrated with a react application.

**obs:Para que não se tenha problemas de [circular imports python](https://stackoverflow.com/questions/744373/circular-or-cyclic-imports-in-python) e melhor organização da app, foi implementado o pattern factory**

# Contains

This application has some cool features implemented:
- flask CLI
- flask SQL-Alchemy/SQLite
- Makefile -> a tool that can help like npm start and npm install packges
- python-dotenv
- factory-structure to flask (avoid circular improts)
- dataclass 
- Enum
- comments for all
- api request(mercado bitcoin)
- api 
- [] docker

Required to implement:
- integrate with React App
- hook
- flask migrate(migrate)
- flask auth(authorization)
- flask marshmallow (serialize)
- pytest
- Doc(Restful)


# Structure

.gitignore
Makefile  
requirements-dev.txt 
requirements.txt 
setup.py 
./wallet 
├── ext
│   ├── api 
│   │   ├── main.py
│   │   └── services
│   ├── cli
│   ├── config
│   ├── db
│   └──  migrate
├── wallet.db
├── .env
├── bundle_api
└── app.py

modules:
- api -> routes and services
- cli -> cli use with flask
- config -> configs for flask
- db -> models and sql alchemy 
- migrate -> not implemented

files:
- wallet.db ->
- .env - pythn-dotenv
- bundle_api -> insomnia collection for tests
- app.py -> initial file

# Run(dockerfile)
- run the image and jump for step 5
```bash
#example
docker build -t williamyizima/api-flask-crip
docker run --network=host -p 5000:5000 williamyizima/api-flask-crip
```

# Run(no dockerfile)

1. create a virtual env:
In the your path(linux)
```bash
virtualenv -p python3 ENV
source ENV/bin/activate
```

2. install dependencies:
```bash
make install
```

3. Create a .env(only tests):
```bash
echo "SECRET_KEY='xxx'" > ./wallet/.env
```

4. Test db:
```bash
make create-db
# FLASK_APP=wallet/app.py flask create-db
# criei a tabela conforme solicitado

make list-db
#lista de usuários vazia

make create-fake-data
#Foi a descrição:data fake e o amount:5.2

make list-db
#lista de registros: [{'description': 'data fake', 'amount': 5.2, 'created_at': '08/16/2021'}]
```

5. Import the collection in insomnia or:
```
#populate with bitcoin
curl --request POST \
  --url 'http://localhost:5000/api/populate?coin=bitcoin'
```

```
#populate with chainlink
curl --request POST \
  --url 'http://localhost:5000/api/populate?coin=bitcoin'
```

```
#view all data
curl --request GET \
  --url http://localhost:5000/api/
```