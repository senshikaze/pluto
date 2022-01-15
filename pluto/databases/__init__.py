# Pluto ORM Database integrations
# CC0 1.0 Universal

from abc import abstractmethod

from sqlite import PlutoDatabaseSqlite

DATABASE_TYPES = {
    "sqlite": "PlutoDatabaseSqlite"
}


class PlutoDatabase:
    def __init__(self, db_type: str):
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
    
    @abstractmethod
    def insert(self, query: str, params: dict) -> int:
        raise NotImplemented("`insert` method should have been implemented")
    
    @abstractmethod
    def select(self, query: str, params: dict, limit: int = 0) -> dict:
        raise NotImplemented("`select` method should have been implemented")

    @abstractmethod
    def select_row(self, query: str, params: dict) -> dict:
        raise NotImplemented("`select_row` method should have been implemented")
    
    @abstractmethod
    def update(self, query: str, params: dict) -> int:
        raise NotImplemented("`update` method should have been implemented")

