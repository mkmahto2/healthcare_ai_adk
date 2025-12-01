FROM python:3.11-slim

WORKDIR /app

# Install system deps for optional image processing (kept minimal)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy project files
COPY .. /app
WORKDIR /app/deploy

# Install Python deps
RUN python -m pip install --upgrade pip
RUN python -m pip install -r requirements.txt

ENV PYTHONUNBUFFERED=1
EXPOSE 8080

CMD ["gunicorn", "-b", "0.0.0.0:8080", "app:app", "--workers", "1", "--threads", "4"]
