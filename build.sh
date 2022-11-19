#!/bin/bash

# Build the project
echo "Building the project..."
python3.9 -m pip install -r requirements.txt

# Run the project
echo "Make migrations"
cd carbonaltdel
python3.9 manage.py makemigrations --noinput
python3.9 manage.py migrate --noinput

echo "Collect static files"
cd carbonaltdel
python3.9 manage.py collectstatic --noinput --clear

