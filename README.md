Commands to run

# Database related
python3 manage.py makemigrations

python3 manage.py makemigrations  --dry-run --verbosity 3

python3 manage.py migrate

# admin related
python3 manage.py createsuperuser


# run server
python3 manage.py runserver


# coverage report
coverage run --omit=*/venv/* manage.py test

coverage report