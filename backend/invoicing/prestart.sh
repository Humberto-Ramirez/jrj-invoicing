#! /usr/bin/env bash

# Let the DB start
python src/pre_start.py

# Run migrations
alembic upgrade head

# Create initial data in DB
python src/initial_data.py
