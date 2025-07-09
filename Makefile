

runserver-local:
	py manage.py runserver --settings=settings.local

runserver-prod:
	py manage.py runserver --settings=settings.prod

migrate:
	py manage.py migrate --settings=settings.local

makemigrations:
	py manage.py makemigrations --settings=settings.local