first commit

# Description
api to integrate with a react application

**obs:Para que não se tenha problemas de [circular imports python](https://stackoverflow.com/questions/744373/circular-or-cyclic-imports-in-python) e melhor organização da app, foi implementado o pattern factory**

# Contains

This application has some cool features implemented:
- flask CLI
- flask SQL-Alchemy/SQLite
- Makefile -> a tool that can help like npm start and npm install packges
- python-dotenv
- factory-structure to flask (avoid circular improts)
- dataclass 
- [] api request
- [] api 
- [] hook
- [] docker
- [] comments for all

Required to implement:
- flask migrate(migrate)
- flask auth(authorization)
- flask marshmallow (serialize)


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