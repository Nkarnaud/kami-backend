# kami-backend

This is app can run easily in a docker environment. Dependency management is done with poetry.
if using docker make use ture you docker engine install on your computer and running the environment.

## install docker
https://docs.docker.com/engine/install/#server

# content of environment file

    DJANGO_DEBUG=1
    DJANGO_SECRET_KEY=secretkey123
    
    DB_DATABASE_NAME=
    DB_USER=
    DB_PASSWORD=
    DB_HOST=
    DB_PORT=

## Build and run the services on docker
 to build and run the services on docker, there are couples of make command defined in the makefile

### Build the docker services, run this command.
  -     make build

Before running the services, you must make sure you have your database setup and running

## database setup
connect to the db container using the following command

    docker exec -it chef_mode_db bash

### connet to psql using the following command

    psql -U kami_db
### create a new user and password for the db

    CREATE USER kamibackend WITH PASSWORD 'kami_db';

### create a new database for the db
    CREATE DATABASE kamibackend_db OWNER kamibackend;

### Run migration

    make migration

once migration is all set you are now ready to go


### run the services, using this command.
  -     make runserver
