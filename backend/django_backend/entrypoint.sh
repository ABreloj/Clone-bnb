#!/bin/sh

if ["$DATABASE" = "postgres"] 
then
    echo "Check if database ir running..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
        sleep 0.1
    done

    echo "La base de datos esta corriendo"
fi

python manage.py makemigrations
python manage.py migrate

exec "$@"