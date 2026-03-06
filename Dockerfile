# Stage 1 - builder
FROM python:3.11-slim AS builder
WORKDIR /app
COPY requirements.txt .

# Install dependencies globally (avoid ~/.local)
RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Stage 2 - runtime
FROM python:3.11-slim
WORKDIR /app

# Copy installed packages from builder
COPY --from=builder /usr/local /usr/local
COPY . .

# Create non-root user
RUN useradd -m appuser \
    && chown -R appuser:appuser /app

USER appuser

# Gunicorn command
CMD ["gunicorn", "config.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "3", "--timeout", "120"]