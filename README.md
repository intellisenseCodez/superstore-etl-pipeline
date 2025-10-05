# Superstore Data Pipeline with dbt and Docker

Build a fully containerized ELT pipeline with Python, PostgreSQL, and DBT, orchestrated via Docker Compose.



Build Image

```bash
docker-compose up --build -d
docker-compose down -v
```

dbt init
```bash
dbt init --project-name dbt_store
```