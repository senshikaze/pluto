# Pluto ORM Database integrations
# CC0 1.0 Universal

from abc import abstractmethod
from typing import Any

DATABASE_TYPES = {
    "sqlite": "PlutoDatabaseSqlite"
}


class PlutoDatabase:
    def __init__(self, db_type: str = None):
        if db_type is not None:
            if db_type not in DATABASE_TYPES:
                raise NotImplemented(f"{db_type} has not been implemented")
            return DATABASE_TYPES[db_type]()
    
    @abstractmethod
    def load(self, database_info: dict[str, str]):
        raise NotImplemented("`load` method should have been implemented")

    @abstractmethod
    def connect(self) -> None:
        raise NotImplemented("`connect` method should have been implemented")
    
    @abstractmethod
    def close(self) -> None:
        raise NotImplemented("`close` method should have been implemented")
    
    ###
    # Abstract methods for generic database actions
    # These are made availble for internal use, and should 
    # not be used by Pluto users unless a specific need arises
    #

    @abstractmethod
    def create_table(self, query: str) -> None:
        raise NotImplementedError("`create_table` method should have been implemented")

    @abstractmethod
    def insert_one(self, query: str, params: list) -> Any:
        raise NotImplementedError("`insert` method should have been implemented")
    
    @abstractmethod
    def select(self, query: str, params: list, limit: int = 0) -> dict:
        raise NotImplementedError("`select` method should have been implemented")

    @abstractmethod
    def select_row(self, query: str, params: list) -> dict:
        raise NotImplementedError("`select_row` method should have been implemented")
    
    @abstractmethod
    def update(self, query: str, params: list) -> int:
        raise NotImplementedError("`update` method should have been implemented")

    ###
    # Abstract methods for use by callers and Pluto users
    #