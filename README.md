# WeatherAppDjango
All required features and an optional feature where user can login and save favourite location has been added.

## Setup

Clone the repo on your system using

```bash
git clone https://github.com/Harshit-2000/WeatherAppDjango.git
```

```bash
cd WeatherAppDjango
```

Create a virtual environment

```bash
pip install virtualenv
python -m venv env
```

Activate a virtual env

```bash
.\env\script\activate
```

Installing Requirements

```bash
pip install -r requirements.txt
```

## Migrate Project to the Database

Run the following command
```bash
python manage.py makemigrations
python manage.py migrate
```

## Run Project
```bash
python manage.py runserver
```
