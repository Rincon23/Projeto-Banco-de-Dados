from flask import Flask, request, redirect
import sqlite3

app = Flask(__name__)

#Criar tabela se ela não existir
def CriarTabelaMaterial():
    banco = sqlite3.connect('Dados.db')
    cursor = banco.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Material (
        IdMaterial INTEGER PRIMARY KEY AUTOINCREMENT,
        Data TEXT,
        Descricao TEXT,
        VlMaterial REAL
    )
    """)

    banco.commit()
    banco.close()

@app.route("/AddMaterial", methods=["POST"])
def AddMaterial():
    Data = request.form["Data"]
    Descricao = request.form["Descricao"]
    VlMaterial = request.form["VlMaterial"]

    conn = sqlite3.connect("Dados.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Material (Data, Descricao, VlMaterial) VALUES (?, ?, ?)", (Data, Descricao, VlMaterial))
    conn.commit()
    conn.close()

    return redirect("/VisualizacaoBanco")

#Selecionando todas as pessoas
def SelecionarTodosOsMateriais():
    conn = sqlite3.connect("Dados.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Material")
    data = cursor.fetchall()
    conn.close()
    return data