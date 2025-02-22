from flask import Flask, request, redirect
import sqlite3

app = Flask(__name__)

def CriartabelaObra():
    banco = sqlite3.connect('TabelaObra.db')
    cursor = banco.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Obra (
        IdObra INTEGER PRIMARY KEY AUTOINCREMENT,
        Nome TEXT NOT NULL,
        DataInicio TEXT NOT NULL,
        DataTermino TEXT NOT NULL
    )
    """)

    banco.commit()
    banco.close()

def BancoObra():
    conn = sqlite3.connect("TabelaObra.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Obra")
    BancoObra = cursor.fetchall()
    conn.close()
    return BancoObra

@app.route("/AddObra", methods=["POST"])
def AddObra():
    Nome = request.form["Nome"]
    DataInicio = request.form["DataInício"]
    DataTermino = request.form["DataTermino"]

    conn = sqlite3.connect("TabelaObra.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Obra (Nome, DataInicio, DataTermino) VALUES (?, ?, ?)", (Nome, DataInicio, DataTermino))
    conn.commit()
    conn.close()

    return redirect("/Adicionador")