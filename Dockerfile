# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Install git
RUN apt-get update && apt-get install -y git

# Copy the requirements.txt file into the container
COPY requirements.txt /app/

# Install the Python dependencies
RUN pip install --no-cache-dir --prefer-binary -r requirements.txt

# Copy the FastAPI app code into the container
COPY API.py /app/

# Expose the port that the app will run on (default FastAPI port)
EXPOSE 8080

# Set the command to run your FastAPI app with Uvicorn
CMD ["uvicorn", "API:app", "--host", "0.0.0.0", "--port", "8080"]
