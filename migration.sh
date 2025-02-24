#!/bin/bash

# Check if both parameters are provided
if [ $# -ne 2 ]; then
    echo "Usage: ./migrate.sh <app_name> <migration_name>"
    exit 1
fi

APP_NAME=$1
MIGRATION_NAME=$2

# Run Django makemigrations with the provided parameters
python manage.py makemigrations $APP_NAME --name $MIGRATION_NAME
