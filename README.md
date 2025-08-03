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

to execute index.html on windows just double click and it will work but on linux distro it behaves differently
# The problem is that coverage.py’s HTML report uses relative file paths, but when you click on them, your browser may try to interpret them as if they were URLs (or blocked local file access for security reasons).

Ways to fix it
1. Serve it with a local web server (Recommended)

From inside your Django project root (where htmlcov/ is):
cd htmlcov
python3 -m http.server 8000

Then open your browser and go to:
http://localhost:8000

Now the links will work corrrectly