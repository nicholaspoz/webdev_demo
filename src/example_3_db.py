import sqlite3
from flask import g


def initialize():
    with _database() as db:
        db.execute(
            """
            CREATE TABLE IF NOT EXISTS count (
                id INTEGER PRIMARY KEY,
                count INTEGER NOT NULL
            );
            """
        )
        if get_count() is None:
            print("Initializing counter")
            db.execute("INSERT INTO count VALUES (1, 0)")


def get_count():
    with _database() as db:
        result = db.execute("SELECT count FROM count WHERE id = 1").fetchone()

        return result[0] if result is not None else None


def increment():
    with _database() as db:
        db.execute("UPDATE count SET count = count + 1 WHERE id = 1")


def reset():
    with _database() as db:
        db.execute("UPDATE count SET count = 0 WHERE id = 1")


def close_connection(exception):
    db = getattr(g, "_database", None)
    if db is not None:
        db.close()


def _database():
    db = getattr(g, "_database", None)
    if db is None:
        db = g._database = sqlite3.connect("example_3.db")
    return db
