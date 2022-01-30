import os
import pytest
import shutil
import sqlite3

from pluto.databases.implementation.sqlite import PlutoDatabaseSqlite

@pytest.fixture()
def pluto_db():
    db = PlutoDatabaseSqlite()
    db.load({"location": ":memory:"})
    db.connect()
    db.db_create_table("""CREATE TABLE test_table (
        id INTEGER PRIMARY KEY, name TEXT)"""
    )
    yield db
    db.close()

# Load, connect, close
def test_sqlite_load():
    db = PlutoDatabaseSqlite()
    db.load({"location": ":memory:"})
    assert ":memory:" == db._db_location


def test_sqlite_connect():
    db = PlutoDatabaseSqlite()
    db.load({"location": ":memory:"})
    db.connect()
    assert isinstance(db._db_object, sqlite3.Connection)


def test_sqlite_close():
    db = PlutoDatabaseSqlite()
    db.load({"location": ":memory:"})
    db.connect()
    assert isinstance(db._db_object, sqlite3.Connection)
    db.close()
    assert db._db_object is None

# pluto db functions

# raw db functions
def test_sqlite_create_table():
    db = PlutoDatabaseSqlite()
    db.load({"location": ":memory:"})
    db.connect()
    db.db_create_table("""
        CREATE TABLE test_table (
            id INTEGER PRIMARY KEY,
            name TEXT
        )"""
    )
    rowid = db.db_insert_one(
        "INSERT INTO test_table (name) VALUES (?)",
        ["testname"]
    )
    assert rowid == 1
    row = db.db_select_row(
        "SELECT * FROM test_table WHERE id = ?",
        [rowid]
    )
    assert row["name"] == "testname"

def test_sqlite_insert(pluto_db: PlutoDatabaseSqlite):
    rowid = pluto_db.db_insert_one(
        "INSERT INTO test_table (name) VALUES (?)",
        ["testname"]
    )
    assert rowid == 1
    row = pluto_db.db_select_row(
        "SELECT * FROM test_table WHERE id = ?",
        [rowid]
    )
    assert row["name"] == "testname"
