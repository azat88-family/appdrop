from flask import Flask, render_template, request, jsonify
from db import init_db, get_db
from models import create_tables

app = Flask(__name__)
DATABASE = "database.db"

# Inicializa banco
init_db(DATABASE)
create_tables(DATABASE)


@app.route("/")
def index():
    conn = get_db(DATABASE)
    cur = conn.cursor()
    cur.execute("SELECT id, item, quantidade, preco FROM vendas")
    vendas = cur.fetchall()
    conn.close()
    return render_template("index.html", vendas=vendas)


@app.route("/add", methods=["POST"])
def add_venda():
    data = request.get_json()
    item = data.get("item")
    quantidade = data.get("quantidade")
    preco = data.get("preco")

    conn = get_db(DATABASE)
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO vendas (item, quantidade, preco) VALUES (?, ?, ?)",
        (item, quantidade, preco),
    )
    conn.commit()
    conn.close()

    return jsonify({"status": "success"})


@app.route("/update/<int:venda_id>", methods=["POST"])
def update_venda(venda_id):
    data = request.get_json()
    quantidade = data.get("quantidade")
    preco = data.get("preco")

    conn = get_db(DATABASE)
    cur = conn.cursor()
    cur.execute(
        "UPDATE vendas SET quantidade=?, preco=? WHERE id=?",
        (quantidade, preco, venda_id),
    )
    conn.commit()
    conn.close()

    return jsonify({"status": "updated"})


@app.route("/delete/<int:venda_id>", methods=["DELETE"])
def delete_venda(venda_id):
    conn = get_db(DATABASE)
    cur = conn.cursor()
    cur.execute("DELETE FROM vendas WHERE id=?", (venda_id,))
    conn.commit()
    conn.close()
    return jsonify({"status": "deleted"})


if __name__ == "__main__":
    app.run(debug=True)
