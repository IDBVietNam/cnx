# Setting up the project with Docker

This guide will help you set up and run the project using Docker and Docker Compose.

## Requirements

Ensure that you have installed the following software on your machine:

- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/install/)

## Getting Started

Follow these steps to set up and run the project:

### 1. Build and Run the Containers
Use Docker Compose to build and run the containers:

```sh
docker-compose up --build
```
This command will build the Docker images and start the containers defined in the `docker-compose.yml` file.

### 2. Access the Services
Once the containers are up and running, you can access the services:

- Django: http://localhost:8000

### 3. Stop the Containers
To stop the running containers, use the following command:

```sh
docker-compose stop
```

