#! /usr/bin/env bash

# Let the DB start
python src/jrj_invoicing/pre_start.py

# Run migrations
alembic upgrade head

# Create initial data in DB
python src/jrj_invoicing/initial_data.py
