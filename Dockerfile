# Base Python image
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Copy dependency file
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY app.py .

# Set environment variable
ENV APP_ENV=production

# Create non-root user
RUN useradd --create-home appuser

# Change ownership
RUN chown -R appuser:appuser /app

# Run application as non-root user
USER appuser

# Expose application port
EXPOSE 5000

# Start application using Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers", "2", "app:app"]
