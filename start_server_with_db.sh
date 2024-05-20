#!/bin/bash

# Drop the development database if it exists
sqlite3 states.db < drop_dev_database.sql

# Create the development database and initialize it
sqlite3 states.db < main_0.sql

# Start the Flask server
export FLASK_APP=main_0.py
flask run --host=0.0.0.0 --port=5000
