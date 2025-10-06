#Use a base Python image
FROM python:3.10-slim

# Install dbt and dbt-postgres
RUN pip install dbt-core dbt-postgres

# Set the working directory inside the container
WORKDIR /src/dbt

# Copy profile.yml
COPY profiles.yml /root/.dbt/profiles.yml

# Copy your dbt project files into the container
COPY ./dbt .

# Default command to run if no other command is specified
CMD ["bash", "-c", "\
    echo '🚀 Running dbt build...'; \
    dbt deps --profiles-dir /root/.dbt; \
    dbt build --profiles-dir /root/.dbt; \
    echo '✅ dbt build complete.'; \
    tail -f /dev/null \
"]