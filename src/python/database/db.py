import sqlite3
from sqlite3 import Connection

from flask import g

DATABASE = './../../../test_todos'


def get_db() -> Connection:
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db


# @app.teardown_appcontext
# def close_connection(exception) -> None:
#     db = getattr(g, '_database', None)
#     if db is not None:
#         db.close()

# TODO Testing Purposes need to have a in-memory db

def change_to_memory_database() -> None:
    pass
