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
        Nome TEXT NOT NULL UNIQUE,
        Salario REAL NOT NULL,
        FOREIGN KEY (IdObra) REFERENCES Obra(IdObra) ON DELETE CASCADE
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
    try:
        IdObra = request.form["IdObra"]
        Nome = request.form["Nome"]
        Salario = request.form["Salario"]

        conn = sqlite3.connect("BancoDeDados.db")
        cursor = conn.cursor()
        cursor.execute("PRAGMA foreign_keys = ON;")
        cursor.execute("INSERT INTO Funcionario (IdObra, Nome, Salario) VALUES (?, ?, ?)", (IdObra, Nome, Salario))
        conn.commit()
        conn.close()
    except sqlite3.Error as erro:
        print("Erro ao adicionar: ", erro)
    return redirect("/Adicionador")

@app.route("/DeleteFuncionario", methods=["POST"])
def DeleteFuncionario():
    try:
        Nome = request.form["Nome"]

        banco = sqlite3.connect('BancoDeDados.db')
        cursor = banco.cursor()
        cursor.execute("PRAGMA foreign_keys = ON;")
        cursor.execute("DELETE from Funcionario WHERE Nome = ?", (Nome,))

        banco.commit() 
        banco.close()
        print("Os dados foram removidos")
    except sqlite3.Error as erro:
        print("Erro ao excluir: ", erro)
    return redirect("/Adicionador") 