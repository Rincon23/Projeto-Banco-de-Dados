from flask import Flask, render_template, request, redirect
import sqlite3
import webview

import sqlite3

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


app = Flask(__name__)



windows = webview.create_window('Projeto Banco', app, width = 1900, height=900, resizable=True, confirm_close=False)


@app.route("/")
def homepage():
    return render_template("homepage.html")

@app.route("/Pessoas")
def pessoas():
    return render_template("Pessoas.html")

@app.route("/Usuarios/<nome_usuario>")
def usuarios(nome_usuario):
    return render_template("Usuarios.html", nome_usuario=nome_usuario)


#conectando meu banco
def get_data():
    conn = sqlite3.connect("primeiro_banco.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM pessoas")
    data = cursor.fetchall()
    conn.close()
    return data

#Criando a pagina Banco

@app.route("/Banco")
def Banco():
    pessoas = get_data()
    return render_template("Banco.html", pessoas=pessoas)


#Adicionando ao Banco

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

    return redirect("/Banco")  # Redireciona para a página inicial

#Deletando do Banco

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

# colocar o site no ar
if __name__ == "__main__":
    webview.start()
    #app.run(debug=True)

