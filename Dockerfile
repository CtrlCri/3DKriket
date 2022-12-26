# Pull base image
FROM python:3.11.0-alpine3.17

# Set environment variables
ENV PYTHONUNBAFFERED=1

# Set work directory
WORKDIR /app

# install dependencies
COPY ./requirements.txt ./
RUN pip install -r requirements.txt

# Copy project
COPY ./ ./