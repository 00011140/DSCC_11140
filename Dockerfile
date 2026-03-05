# Stage 1: Build
FROM python:3.11-slim AS builder

# Non-root user
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --upgrade pip \
    && pip install --user -r requirements.txt

# Copy project files
COPY . .

# Stage 2: Production image
FROM python:3.11-slim

# Non-root user
RUN adduser --disabled-password appuser
USER appuser

WORKDIR /app

# Copy dependencies from builder
COPY --from=builder /root/.local /home/appuser/.local
COPY --from=builder /app /app

# Ensure local bin is in PATH
ENV PATH=/home/appuser/.local/bin:$PATH

# Collect static files
RUN python manage.py collectstatic --noinput

# Gunicorn
CMD ["gunicorn", "config.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "3"]