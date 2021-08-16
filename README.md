first commit

# Description
api to integrate with a react application

# Contains

This application has some cool features implemented:
- flask CLI
- flask SQLite
- flask SQL-Alchemy
- Makefile -> a tool that can help like npm start and npm install packges
- python-dotenv
- factory-structure to flask (avoid relative improts)

Required to implement:
- flask migrate
- flask auth


# Run

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

3. Create a .env:
```bash
echo "SECRET_KEY='xxx'" > ./wallet/.env
```

4. Test db:
```bash
flask create-db
flask list-gains
#lista de usuários vazia
flask add-user -de="testando" -am=5.1
```