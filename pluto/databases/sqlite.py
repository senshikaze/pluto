# Pluto ORM Database integrations
# CC0 1.0 Universal

from . import PlutoDatabase

class PlutoDatabaseSqlite (PlutoDatabase):
    _db_location: str
    _db_username: str
    _db_password: str

    def load(self, database_config: dict[str, str]) -> None:
        if "location" not in database_config:
            raise ValueError("Missing `location` in `database_config`")
        if "username" not in database_config:
            raise ValueError("Missing `username` in `database_config`")
        if "password" not in database_config:
            raise ValueError("Missing `password` in `database_config`")
        self._db_location = database_config["location"]
        self._db_username = database_config["username"]
        self._db_password = database_config["password"]
    
    def connect(self):
        pass
