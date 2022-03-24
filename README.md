# django_experiment_application
## Getting Started
```
git clone git@github.com:KarmaComputing/django_experiment_application.git
cd django_experiment_application
python3 -m venv venv
. venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
python3 manage.py migrate
python3 manage.py runserver

```
navigate to 127.0.0.1:8000

## Creating SuperUser 
```
python3 manage.py createsuperuser
```

## To Access the application
navigate to 127.0.0.1:8000/admin  
Login as admin  
Create 2 groups: members, manager  
Create 2 users and assign each user to a group  
have fun! 
