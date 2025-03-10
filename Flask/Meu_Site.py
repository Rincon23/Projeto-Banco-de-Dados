from flask import Flask, render_template
from Senha import Confirmacao
from BancoMaterial import CriarTabelaMaterial, AddMaterial, SelecionarTodosOsMateriais
import webview

app = Flask(__name__)

#Criar tabela se ela não existir
CriarTabelaMaterial()

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

@app.route("/VisualizacaoBanco")
def VisualizacaoBanco():
    Materiais = SelecionarTodosOsMateriais()
    return render_template("VisualizacaoBanco.html", Materiais=Materiais)

@app.route("/AddMateriais")
def OOAddMateriais():
    Materiais = SelecionarTodosOsMateriais()
    return render_template("AddMateriais.html", Materiais=Materiais)

#Acessando funções

@app.route("/Confirmacao", methods=["POST"])
def confirmar_usuario():
    return Confirmacao()

@app.route("/AddMaterial", methods=["POST"])
def OOAddMaterial():
    return AddMaterial()

# colocar o site no ar

if __name__ == "__main__":
    #webview.start()
    app.run(debug=True)
    
