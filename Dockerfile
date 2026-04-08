# Use a slim Python image for efficiency
FROM python:3.10-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /app

# Install dependencies
COPY project1/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project
COPY project1/src/ .

# Expose port
EXPOSE 8080

# Run the server
CMD ["python", "main.py"]
