import os
import pytest
import shutil
import sqlite3

from pluto.databases.sqlite import PlutoDatabaseSqlite


@pytest.fixture(scope="module")
def cleanup():
    files = os.path.join(os.getcwd(), "files")
    if not os.path.isdir(files):
        os.mkdir(files)
    yield files
    shutil.rmtree(files, ignore_errors=True)


@pytest.fixture()
def create_db(cleanup):
    db = os.path.join(cleanup, "sqlite.db")
    yield db
    os.unlink(db)


@pytest.fixture()
def pluto_db(create_db):
    db = PlutoDatabaseSqlite()
    db.load({"location": create_db})
    db.connect()
    db.create_table("""CREATE TABLE test_table (
        id INTEGER PRIMARY KEY, name TEXT)"""
    )
    yield db
    db.close()


def test_sqlite_load():
    db = PlutoDatabaseSqlite()
    db.load({"location": "testdb"})
    assert "testdb" == db._db_location


def test_sqlite_connect(create_db):
    db = PlutoDatabaseSqlite()
    db.load({"location": create_db})
    db.connect()
    assert isinstance(db._db_object, sqlite3.Connection)


def test_sqlite_close(create_db):
    db = PlutoDatabaseSqlite()
    db.load({"location": create_db})
    db.connect()
    assert isinstance(db._db_object, sqlite3.Connection)
    db.close()
    assert db._db_object is None

def test_sqlite_create_table(create_db):
    db = PlutoDatabaseSqlite()
    db.load({"location": create_db})
    db.connect()
    db.create_table("""
        CREATE TABLE test_table (
            id INTEGER PRIMARY KEY,
            name TEXT
        )"""
    )
    rowid = db.insert_one(
        "INSERT INTO test_table (name) VALUES (?)",
        ["testname"]
    )
    assert rowid == 1
    row = db.select_row(
        "SELECT * FROM test_table WHERE id = ?",
        [rowid]
    )
    assert row["name"] == "testname"

def test_sqlite_insert(pluto_db: PlutoDatabaseSqlite):
    rowid = pluto_db.insert_one(
        "INSERT INTO test_table (name) VALUES (?)",
        ["testname"]
    )
    assert rowid == 1
    row = pluto_db.select_row(
        "SELECT * FROM test_table WHERE id = ?",
        [rowid]
    )
    assert row["name"] == "testname"
