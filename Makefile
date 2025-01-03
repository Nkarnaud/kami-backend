# DOCKER
build:
	@docker-compose build backend

up:
	@docker-compose run --service-ports -d --name backend backend
	@docker-compose run --service-ports -d --name psql psql

down:
	@docker-compose down --remove-orphans

rebuild: down build up

restart:
	@docker restart psql backend

runserver:
	@docker exec -it backend bash -c "./manage.py runserver 0.0.0.0:8000"

exec:
	@docker exec -it backend bash


path?=

test:
	@docker exec -it backend bash -c "pytest -p no:warnings $(path)"

db_connect:
	@docker exec -it psql bash


makemigrations:
	@docker exec -it backend python manage.py makemigrations

migrate:
	@docker exec -it backend python manage.py migrate
