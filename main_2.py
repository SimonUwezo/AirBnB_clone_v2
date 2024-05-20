#!/bin/bash
psql -U your_database_user -d your_database_name -f main_2.sql
python3 main_2.py
