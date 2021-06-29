#!/bin/bash
rm -rf alinasclosetapi/migrations
rm db.sqlite3
python manage.py makemigrations alinasclosetapi
python manage.py migrate
python manage.py loaddata users
python manage.py loaddata tokens
python manage.py loaddata looks
python manage.py loaddata retailers
python manage.py loaddata categories
python manage.py loaddata pieces
python manage.py loaddata shoppinglists
python manage.py loaddata userpieces