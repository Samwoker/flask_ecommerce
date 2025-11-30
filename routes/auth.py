import sqlite3

from flask import Flask ,Blueprint

auth_bp = Blueprint('auth',__name__)


def get_db():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    return conn



