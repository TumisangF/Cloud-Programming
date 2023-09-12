# The code below contains instructions on how to build the docker image

# Use the official Python image as the base
FROM python:3.8-slim

# Set the working directory
WORKDIR /app

# Copy the application files into the container
COPY . /app

# Install Flask, pandas, and scikit-learn
RUN pip install Flask pandas scikit-learn

# Expose the port on which the app will run
EXPOSE 80

# Set environment variables for Flask
ENV NAME World

# Set the entry point for the container
CMD ["python", "app.py"]
