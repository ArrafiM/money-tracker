# money-tracker
tracking my money

## pip installation
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install
or
download get-pip.py
```bash
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
```

install pip
```bash
python get-pip.py
```
you must install python in youre computer

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

Instal FastAPI
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

## Api Docs
open in your browser http://localhost:8000/docs
