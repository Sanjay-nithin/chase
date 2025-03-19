# Use Python base image
FROM python:3.10

# Set working directory inside container
WORKDIR /app

# Copy project files into the container
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 8000 (Django default)
EXPOSE 8000

# Run Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
