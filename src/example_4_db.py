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


def set_count(value):
    with _database() as db:
        db.execute(f"UPDATE count SET count = ? WHERE id = 1", (value,))


def close_connection(exception):
    db = getattr(g, "_database", None)
    if db is not None:
        db.close()


def _database():
    db = getattr(g, "_database", None)
    if db is None:
        db = g._database = sqlite3.connect("example_4.db")
    return db
