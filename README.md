first commit

# Description

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