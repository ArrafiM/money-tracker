# money-tracker
tracking my money

## create virtualenv
```bash
python -m venv nama-environment
```

## masuk virualenv
in bash
```bash
virtualenv nama-environment
```
```bash
windows
. nama-environment/Scripts/activate
```

linux
```bash
source venv/bin/activate
```
------------------------------

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install

```bash
pip install "fastapi[all]"
```

## instal requirements
```bash
pip install -r requirements.txt
```

after instal
update .env file and create your database

-------------------------

## running program
```bash
uvicorn app.main:app --reload
```
database migration will runnning automatically when your run the program
