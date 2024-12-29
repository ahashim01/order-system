# Use official Python image
FROM python:3.12

# Install system dependencies
RUN apt-get update && apt-get install -y \
    libpq-dev gcc python3-dev musl-dev && \
    apt-get clean

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy the rest of the project
COPY . .

# Collect static files
RUN python manage.py collectstatic --noinput

# Expose the port
EXPOSE 8000

# Default command
CMD ["gunicorn", "--workers=3", "--bind=0.0.0.0:8000", "use_case_project.wsgi:application"]
