from flask import Flask, request, redirect
import sqlite3

app = Flask(__name__)

def CriarTabelaFuncionario():
    banco = sqlite3.connect('BancoDeDados.db')
    cursor = banco.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Funcionario (
        IdFuncionario INTEGER PRIMARY KEY AUTOINCREMENT,
        IdObra INTEGER NOT NULL,
        Nome TEXT NOT NULL,
        Salario REAL NOT NULL,
        FOREIGN KEY (IdObra) REFERENCES Obra(IdObra)
    )
    """)

    banco.commit()
    banco.close()

def BancoFuncionario():
    conn = sqlite3.connect("BancoDeDados.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Funcionario")
    BancoFuncionario = cursor.fetchall()
    conn.close()
    return BancoFuncionario

@app.route("/AddFuncionario", methods=["POST"])
def AddFuncionario():
    IdObra = request.form["IdObra"]
    Nome = request.form["Nome"]
    Salario = request.form["Salario"]

    conn = sqlite3.connect("BancoDeDados.db")
    cursor = conn.cursor()
    cursor.execute("PRAGMA foreign_keys = ON;")
    cursor.execute("INSERT INTO Funcionario (IdObra, Nome, Salario) VALUES (?, ?, ?)", (IdObra, Nome, Salario))
    conn.commit()
    conn.close()
    
    return redirect("/Adicionador")