from flask import Flask, request, redirect
import sqlite3

app = Flask(__name__)

def CriarTabelaObra():
    banco = sqlite3.connect('BancoDeDados.db')
    cursor = banco.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Obra (
        IdObra INTEGER PRIMARY KEY AUTOINCREMENT,
        Nome TEXT NOT NULL UNIQUE,
        DataInicio TEXT NOT NULL,
        DataTermino TEXT NOT NULL
    )
    """)

    banco.commit()
    banco.close()

def BancoObra():
    conn = sqlite3.connect("BancoDeDados.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Obra")
    BancoObra = cursor.fetchall()
    conn.close()
    return BancoObra

@app.route("/AddObra", methods=["POST"])
def AddObra():
    try:
        Nome = request.form["Nome"]
        DataInicio = request.form["DataInício"]
        DataTermino = request.form["DataTermino"]

        conn = sqlite3.connect("BancoDeDados.db")
        cursor = conn.cursor()
        cursor.execute("PRAGMA foreign_keys = ON;")
        cursor.execute("INSERT INTO Obra (Nome, DataInicio, DataTermino) VALUES (?, ?, ?)", (Nome, DataInicio, DataTermino))
        conn.commit()
        conn.close()
    except sqlite3.Error as erro:
        print("Erro ao adicionar: ", erro)
    return redirect("/Adicionador")

@app.route("/DeleteObra", methods=["POST"])
def DeleteObra():
    try:
        Nome = request.form["Nome"]

        banco = sqlite3.connect('BancoDeDados.db')
        cursor = banco.cursor()
        cursor.execute("PRAGMA foreign_keys = ON;")
        cursor.execute("DELETE from Obra WHERE Nome = ?", (Nome,))

        banco.commit() 
        banco.close()
        print("Os dados foram removidos")
    except sqlite3.Error as erro:
        print("Erro ao excluir: ", erro)
    return redirect("/Adicionador") 