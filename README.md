# Wordle in Python

## Setup

Add .env file with
```yaml
POSTGRES_USER=
POSTGRES_PASSWORD=
POSTGRES_HOST=localhost
POSTGRES_PORT=5632
POSTGRES_DB=
```

Run `docker-compose up -d database`

## Migrations

Run: `alembic upgrade head`

Create: `alembic revision --autogenerate -m "message"`

Init new DB: `alembic -x data=true upgrade head`