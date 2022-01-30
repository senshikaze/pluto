# Pluto ORM Database integrations
# CC0 1.0 Universal

from sqlite3 import Connection
import sqlite3
from typing import Any, Dict

from .. import PlutoDatabase

class PlutoDatabaseSqlite (PlutoDatabase):
    _db_location: str
    _db_object: Connection

    def load(self, database_config: Dict[str, str]) -> None:
        if "location" not in database_config:
            raise ValueError("Missing `location` in `database_config`")
        self._db_location = database_config["location"]

    def connect(self):
        self._db_object = sqlite3.connect(self._db_location)
        self._db_object.row_factory = sqlite3.Row
    
    def close(self):
        self._db_object.close()
        self._db_object = None

    def db_create_table(self, query: str) -> None:
        self._db_object.execute(query)
    
    def db_insert_one(self, query: str, params: list) -> Any:
        cursor = self._db_object.execute(query, params)
        return cursor.lastrowid
    
    def db_select_row(self, query: str, params: list) -> dict:
        cursor = self._db_object.execute(query, params)
        return cursor.fetchone()
