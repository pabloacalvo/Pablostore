

runserver-local:
	py manage.py runserver --settings=settings.local

runserver-prod:
	py manage.py runserver --settings=settings.prod

migrate:
	py manage.py migrate --settings=settings.local

makemigrations:
	py manage.py makemigrations --settings=settings.local

# Crear dump de la base de datos
# Uso: make copy-db DB_FILE=archivo.sql
copy-db:
	mysqldump -u root pablostore > ${DB_FILE}

# Crear base de datos local
create-local-db:
	echo "CREATE DATABASE pablostore;" | mysql -u root

# Borrar y recrear la base
clear-local-db:
	echo "DROP DATABASE IF EXISTS pablostore; CREATE DATABASE pablostore;" | mysql -u root

# Importar base: borra y recrea antes
# Uso: make import-db DB_FILE=archivo.sql
import-db: clear-local-db import-db-local-db

# Importar desde archivo SQL
import-db-local-db:
	mysql -u root pablostore < ${DB_FILE}


