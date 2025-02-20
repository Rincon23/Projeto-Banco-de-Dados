from flask import Flask, render_template, request, redirect
from Senha import Confirmacao
from Banco import criartabela, add, delete
import sqlite3
import webview

app = Flask(__name__)

criartabela() #Criar tabela se ela não existir

#Configurar janela do pyview
windows = webview.create_window('Projeto Banco', app, width = 1900, height=900, resizable=True, confirm_close=False)

#Acessando templates
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
def Adicionar():
    return add()

#Deletando do Banco

@app.route("/Delete", methods=["POST"])
def Deletando():
    return delete()

#Confirmando a senha

@app.route("/Confirmacao", methods=["POST"])
def confirmar_usuario():
    return Confirmacao()


# colocar o site no ar

if __name__ == "__main__":
    #webview.start()
    app.run(debug=True)
    
