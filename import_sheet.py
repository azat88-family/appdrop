import pandas as pd
import sqlite3
import sys

def import_csv_to_db(csv_url, db_path="database.db"):
    df = pd.read_csv(csv_url)

    conn = sqlite3.connect(db_path)
    cur = conn.cursor()

    # limpa a tabela
    cur.execute("DELETE FROM vendas")

    for _, row in df.iterrows():
        cur.execute(
            "INSERT INTO vendas (item, quantidade, preco) VALUES (?, ?, ?)",
            (row["item"], row["quantidade"], row["preco"]),
        )

    conn.commit()
    conn.close()
    print("Importação concluída!")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python import_sheet.py <URL_CSV>")
    else:
        import_csv_to_db(sys.argv[1])
