# Use a lightweight official Python image
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Copy dependency list and install them
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the script into the container
COPY ingest.py .

# Run the script when the container starts
CMD ["python", "ingest.py"]