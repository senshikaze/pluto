from abc import abstractmethod
from typing import Any, Dict

from pluto.databases.result import PlutoDatabaseResult
from pluto.databases.model import PlutoModel


DATABASE_TYPES = {
    "sqlite": "PlutoDatabaseSqlite"
}


class PlutoDatabase:
    """Database interface for Pluto ORM"""
    def __init__(self, db_type: str = None):
        if db_type is not None:
            if db_type not in DATABASE_TYPES:
                raise NotImplemented(f"{db_type} has not been implemented")
            return DATABASE_TYPES[db_type]()
    
    @abstractmethod
    def load(self, database_info: Dict[str, str]):
        raise NotImplemented("`load` method should have been implemented")

    @abstractmethod
    def connect(self) -> None:
        raise NotImplemented("`connect` method should have been implemented")
    
    @abstractmethod
    def close(self) -> None:
        raise NotImplemented("`close` method should have been implemented")
    
    ###
    # Methods for use by callers and Pluto users
    #

    @abstractmethod
    def insert(self, model: PlutoModel) -> int:
        raise NotImplemented("`insert` method should have been implemented")

    @abstractmethod
    def select(self, model: PlutoModel, rows: int = 1) -> PlutoDatabaseResult:
        raise NotImplemented("`select` method shoud have been implemented")
    
    @abstractmethod
    def update(self, model: PlutoModel) -> int:
        raise NotImplemented("`update` methods should have been implemented")


    ###
    # Methods for generic database actions
    # These are made availble for internal use, and should 
    # not be used by Pluto users unless a specific need arises
    # These functions will return the raw database implementation's 
    # cursor or equivalent
    #

    @abstractmethod
    def db_create_table(self, query: str) -> None:
        raise NotImplementedError("`create_table` method should have been implemented")

    @abstractmethod
    def db_insert_one(self, query: str, params: list) -> Any:
        raise NotImplementedError("`db_insert_one` method should have been implemented")
    
    @abstractmethod
    def db_select(self, query: str, params: list, limit: int = 0) -> dict:
        raise NotImplementedError("`db_select` method should have been implemented")

    @abstractmethod
    def db_select_row(self, query: str, params: list) -> dict:
        raise NotImplementedError("`db_select_row` method should have been implemented")
    
    @abstractmethod
    def db_update(self, query: str, params: list) -> int:
        raise NotImplementedError("`db_update` method should have been implemented")


class PlutoQuery:
    """Query builder for Pluto ORM"""
    def __init__(self):
        pass
    