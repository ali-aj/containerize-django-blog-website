# Django Application with Docker and Docker Compose

This project is a containerized Django application that uses Docker for isolated environments and Docker Compose for easier multi-service orchestration. This README covers the structure, setup, and running of the application.

## Project Structure

- `Dockerfile`: Defines the Docker image for the Django application.
- `docker-compose.yml`: Defines the Docker Compose services for the application, including the Django app and other potential services.
- `db.sqlite3`: SQLite database file for data persistence.
- `db/`: Directory containing the SQLite database, ensuring data persistence even if the container restarts.

## Prerequisites

- **Docker**: Ensure Docker is installed and running.
- **Docker Compose**: Ensure Docker Compose is installed.

---

## Dockerfile

The `Dockerfile` is a multi-stage build that sets up a production-ready Django application. 

### Structure

1. **Base Image**: Starts from `python:3.12-slim` to minimize the image size.
2. **Dependencies**: Installs all dependencies listed in `requirements.txt`.
3. **App Setup**: Copies application code into the container.
4. **Non-Root User**: Creates a non-root user for added security.
5. **CMD**: The container runs Django’s development server.

### Key Commands

```dockerfile
# Use an official Python runtime as the base image
FROM python:3.12-slim as build

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Create a non-root user
RUN addgroup --system django && adduser --system --group django

# Run as the non-root user
USER django

# Start the Django server
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
```

### Building and Running the Docker Image

To build the Docker image:

```bash
docker build -t django-local .
```

To run the Docker container:

```bash
docker run -p 8000:8000 django-local
```

---

## Docker Compose

The `docker-compose.yml` file orchestrates the Django application with other services.

### Structure

- **django-app**: Defines the Django application using the `Dockerfile` and binds it to port 8000.
- **volumes**: Maps the local `db/` directory to ensure SQLite data persists between container restarts.

### Key Commands

```yaml
version: '3.8'

services:
  django-app:
    build:
      context: .
      dockerfile: Dockerfile
    ports:
      - "8000:8000"
    volumes:
      - ./db:/app/db
    environment:
      - DEBUG=1
```

### Running with Docker Compose

Start the application:

```bash
docker-compose up
```

Stop the application:

```bash
docker-compose down
```

---

## Accessing the Application

- Once started, the application is available at `http://localhost:8000`.
- Uploaded files and data are saved in the `db/` directory for persistence.

---

## Additional Notes

- **Database Management**: SQLite is used for development. For production, consider switching to PostgreSQL or MySQL.
- **Security**: This setup is configured for development; always set `DEBUG=0` and add secure settings for production.
  
--- 

## Troubleshooting

- **Port Conflicts**: If port 8000 is in use, change it in the `docker-compose.yml` file.
- **Database Not Found**: Ensure the `db/` directory and `db.sqlite3` file have the correct permissions for persistence.

--- 

This setup provides a simple and efficient way to develop and test a Django application in an isolated environment. Happy coding!