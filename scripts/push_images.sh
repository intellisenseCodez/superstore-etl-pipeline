#!/bin/bash
set -e

DOCKER_USER="horlar"
VERSION="latest"

echo "🔹 Building and pushing ETL app..."
docker build -t $DOCKER_USER/etl_app:$VERSION -f ./docker/etl/Dockerfile
docker push $DOCKER_USER/etl_app:$VERSION

echo "🔹 Building and pushing DBT image..."
docker build -t $DOCKER_USER/dbt_project:$VERSION -f ./docker/dbt/Dockerfile
docker push $DOCKER_USER/dbt_project:$VERSION

echo "✅ All images pushed successfully!"
