# Read & Export Requirements .
FROM python:3.9 as requirements-stage

WORKDIR /tmp
RUN pip install poetry
COPY ./pyproject.toml ./poetry.lock* /tmp/
RUN poetry export -f requirements.txt --output requirements.txt --without-hashes

# App
FROM python:3.9

WORKDIR /code

# Get packages from Requirements Stage
COPY --from=requirements-stage /tmp/requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# Set environment variables.
ENV POSTGRES_SERVER=postgresdb
ENV POSTGRES_USER=postgres
ENV POSTGRES_PASSWORD=P5wF4$stAdm1n
ENV POSTGRES_DB=app

COPY ./src/jrj_invoicing /code/jrj_invoicing

CMD ["uvicorn", "jrj_invoicing.main:app", "--host", "0.0.0.0", "--port", "80"]