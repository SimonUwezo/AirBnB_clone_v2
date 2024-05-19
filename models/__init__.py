#!/usr/bin/python3
"""
Initialize the models package
"""

from os import getenv

# Retrieve the storage type from environment variables
storage_t = getenv("HBNB_TYPE_STORAGE")

# Depending on the storage type, import and initialize the appropriate storage engine
if storage_t == "db":
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()

# Reload the storage to load any existing data
storage.reload()
