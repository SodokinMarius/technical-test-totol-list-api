

#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
echo "waiting for postgresql..."
 while ! nc -z $SQL_HOST $SQL_PORT ; do
    sleep  1.0
 done 
 echo 'PostgreSQL started'

fi

 python manage.py flush --no-input

 python manage.py makemigrations

 python manage.py migrate

exec "$@"