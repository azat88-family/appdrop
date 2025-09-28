import sqlite3

def create_tables(db_path):
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS vendas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            item TEXT,
            quantidade INTEGER,
            preco REAL
        )
    """)
    conn.commit()
    conn.close()
