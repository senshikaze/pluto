from ...pluto.databases.sqlite import PlutoDatabaseSqlite

def testSqliteLoad():
    db = PlutoDatabaseSqlite()
    db.load({"location": "testdb", "username": "testuser", "password": "testpassword"})
    assert "testuser" == db._db_username
