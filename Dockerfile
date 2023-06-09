# 1. Define the official Python base image
FROM python:3.10-slim-bullseye

# 2. set environment vaiables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# 3. Set the working directory
WORKDIR /app

# 4. Install dependencies
COPY requirements.txt /app/
RUN pip install --upgrade pip && pip install -r requirements.txt

# 5. Copy the project code into the container
COPY . /app/

# 6. Expose the port on which the Django app will run
EXPOSE 8000

# 7. Run the Django development server
CMD ['python', 'manage.py', 'runserver'. '0.0.0.0:8000']
