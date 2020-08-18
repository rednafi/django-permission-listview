#!/bin/bash

# Spin up the container and force build
docker-compose down && docker-compose up -d --build

# Run pending migrations
docker-compose exec web python manage.py migrate
