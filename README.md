# NeuroCage Test

NeuroCage test is a Django project designed to showcase my skills as a developer and apply for a position at Neurocage Company. It includes a web application, a PostgreSQL database, an Nginx server, a RabbitMQ message broker, and a Celery worker for background tasks.

![screenshot](./screenshot/screen.jpg)

## Getting started

To run the project locally, you need Docker and Docker Compose installed on your system. Then, follow these steps:

1. Clone this repository to your machine:
```bash
git clone https://github.com/realxoman/neurocage_test.git
```

2. Navigate to the project directory:
```bash
cd neurocage_test
```

3. Copy the example environment file and adjust the settings if necessary:
```bash
cp env.dev .env
```

4. Build and start the containers in detached mode:
```bash
docker-compose up --build -d
```

5. Open your web browser and visit http://localhost to see the web application in action.

## Services

The following services are included in the project:

- web: The Django web application that serves the main functionality of the project. It runs on port 8080 and communicates with the database, the message broker, and the Celery worker.

- db: The PostgreSQL database that stores the data of the application. It is configured with environment variables from the .env file and persists its data in a Docker volume.

- nginx: The Nginx server that acts as a reverse proxy for the web application. It serves static and media files and logs its activity to a local directory.

- rabbit: The RabbitMQ message broker that handles the communication between the web application and the Celery worker. It runs on its default ports 5672 and 15672.

- celery: The Celery worker that executes background tasks asynchronously. It is configured to use the RabbitMQ broker and runs with a concurrency of 10 processes.

## LICENSE
This project is licensed under the GNU General Public License v3.0 - see the [LICENSE](./LICENSE) file for details.
