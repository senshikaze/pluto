# Pluto ORM
# CC0 1.0 Universal

from argparse import ArgumentError
from enum import Enum
from typing import Dict

from pluto.databases import PlutoDatabase


class Pluto:
    _db: PlutoDatabase

    def __init__(self, database_info: Dict[str, str]):
        if "type" not in database_info:
            raise ArgumentError("Missing `type` from `database_info`")
        self._db = PlutoDatabase(database_info["type"])
        self._db.load(database_info)
