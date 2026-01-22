# --- Stage 1: Builder ---
FROM python:3.11-slim as builder

# Avoid writing .pyc files and enable real-time logging
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Install build dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy only the dependency file to leverage Docker cache
COPY pyproject.toml .
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir --target=/app/dependencies .

# --- Stage 2: Final ---
FROM python:3.11-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
# Ensure Python can find our application and dependencies
ENV PYTHONPATH="/app/src:/app/dependencies"

# Copy dependencies from the builder stage
COPY --from=builder /app/dependencies /app/dependencies
# Copy application source code
COPY ./src /app/src

# Create a non-root user to run the application
RUN adduser --disabled-password --gecos "" trencadisuser
USER trencadisuser

# Port to expose the application with FastAPI and Uvicorn
EXPOSE 8000

# Command to run the FastAPI application using Uvicorn
CMD ["python", "-m", "uvicorn", "Infrastructure.Delivery.Http.FastAPI.main:app", "--host", "0.0.0.0", "--port", "8000"]