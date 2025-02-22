from flask import Flask, request, redirect
import sqlite3

app = Flask(__name__)

#Criar tabela se ela não existir
def criartabela():
    banco = sqlite3.connect('primeiro_banco.db')
    cursor = banco.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS pessoas (
        nome TEXT,
        idade INTEGER,
        objeto TEXT
    )
    """)

    banco.commit()
    banco.close()

#Selecionando todas as pessoas
def get_data():
    conn = sqlite3.connect("primeiro_banco.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM pessoas")
    data = cursor.fetchall()
    conn.close()
    return data


#Adicionando dados da tabela
@app.route("/Add", methods=["POST"])
def add():
    nome = request.form["nome"]
    idade = request.form["idade"]
    objeto = request.form["objeto"]

    conn = sqlite3.connect("primeiro_banco.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO pessoas (nome, idade, objeto) VALUES (?, ?, ?)", (nome, idade, objeto))
    conn.commit()
    conn.close()

    return redirect("/Banco")

#Deletando dados da tabela
@app.route("/Delete", methods=["POST"])
def delete():
    try:
        nome = request.form["nome"]

        banco = sqlite3.connect('primeiro_banco.db')

        cursor = banco.cursor()
        cursor.execute("DELETE from pessoas WHERE nome = ?", (nome,))
        banco.commit() 
        banco.close()
        print("Os dados foram removidos")
    except sqlite3.Error as erro:
        print("Erro ao excluir: ", erro)
    return redirect("/Banco")  # Redireciona para a página inicial