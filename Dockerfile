# Dockerfile
FROM python:3.9-slim

# Set environment variables to make Python output more immediate and prevent .pyc file generation
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory inside the container
WORKDIR /app

# First, copy the dependency requirements file
COPY requirements.txt .

# Install all Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy all project source code into the working directory
COPY . .

# Declare the port the container will listen on
EXPOSE 8000