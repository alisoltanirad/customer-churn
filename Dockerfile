# Use the official lightweight Python image.
# https://hub.docker.com/_/python
FROM python:3.11-slim

# Allow statements and log messages to immediately appear in the logs
ENV PYTHONUNBUFFERED True

# Copy local code to the container image
ENV APP_HOME /app
WORKDIR $APP_HOME
COPY requirements.txt ./
COPY src ./

# Install application dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port for the FastAPI application
EXPOSE 8000

# Run the web service on container startup
CMD ["gunicorn", "api.app:application", "-b", "0.0.0.0:8000", "--workers", "1", "--threads", "8", "--timeout", "0"]
