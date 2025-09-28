import sqlite3

def get_db(db_path):
    conn = sqlite3.connect(db_path)
    return conn

def init_db(db_path):
    conn = sqlite3.connect(db_path)
    conn.close()
