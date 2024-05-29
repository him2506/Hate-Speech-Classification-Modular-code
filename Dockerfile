# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /hate

# Copy the requirements.txt file into the container at /app
COPY requirements.txt /hate/

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application's code into the container
COPY . /hate/
COPY . /app.py/
COPY . /Dockerfile
COPY . /setup.py

# Expose the port the app runs on
EXPOSE 8080

# Define environment variable
ENV NAME World

# Run the application when the container launches
CMD ["python", "app.py"]
