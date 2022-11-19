#!/bin/bash

# Build the project
echo "Building the project..."
pythoN3.10 -m pip install -r requirements.txt

# Run the project
echo "Make migrations"
python3.10 manage.py makemigrations --noinput
python3.10 manage.py migrate --noinput

echo "Collect static files"
python3.10 manage.py collectstatic --noinput --clear

