# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Install git and ffmpeg, then clean up apt cache to reduce image size
RUN apt-get update && \
    apt-get install -y git ffmpeg

# Copy only the requirements file first to take advantage of layer caching
COPY requirements.txt /app/

# Install Python dependencies
RUN pip install --no-cache-dir --prefer-binary -r requirements.txt

# Now copy the app code (this ensures changes in the app code don't invalidate pip install)
COPY . /app/

# Expose the port the app will run on (default FastAPI port)
EXPOSE 8080

# Set the command to run your FastAPI app with Uvicorn
CMD ["uvicorn", "API:app", "--host", "0.0.0.0", "--port", "8080"]
