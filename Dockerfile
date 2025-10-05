# Base image
FROM python:3.10-slim

# Set working directory
WORKDIR /src

# Copy and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy code
COPY . /src

# run ETL first, then DBT
CMD bash -c "\
    echo '⏳ Waiting for PostgreSQL initialization...'; \
    echo '🚀 Starting ETL process...'; \
    sleep 10; \
    python3 etl/main.py; \
    echo '✅ ETL pipeline completed successfully.'; \
"

