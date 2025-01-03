# Use an official Python runtime as the base image
FROM python:3.12-slim as build

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory
WORKDIR /app

# Install build dependencies
RUN apt-get update \
    && apt-get install -y --no-install-recommends gcc python3-dev \
    && rm -rf /var/lib/apt/lists/*

# Install dependencies in a separate layer
COPY requirements.txt .
RUN pip install --upgrade pip setuptools wheel \
    && pip install --no-cache-dir -r requirements.txt

# Copy the project files
COPY . .

# Final stage
FROM python:3.12-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory
WORKDIR /app

# Copy installed packages from the build stage
COPY --from=build /usr/local/lib/python3.12/site-packages /usr/local/lib/python3.12/site-packages
COPY --from=build /app /app/

# Create a non-root user
RUN addgroup --system django && adduser --system --group django

# Give rwx permissions to the new user for the /app directory
RUN chown -R django:django /app && chmod -R 755 /app

USER django

# Run the application
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "blogs.wsgi:application"]