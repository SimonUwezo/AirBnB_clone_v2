#!/bin/bash
psql -U your_database_user -d your_database_name -f main_1.sql
python3 main_1.py
