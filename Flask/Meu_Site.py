from flask import Flask, render_template
from Senha import Confirmacao
from Banco import criartabela, add, delete, get_data
from TabelaObra import CriarTabelaObra, BancoObra, AddObra, DeleteObra
from TabelaFuncionario import CriarTabelaFuncionario, BancoFuncionario, AddFuncionario, DeleteFuncionario
import webview

app = Flask(__name__)

#Criar tabela se ela não existir
criartabela() 
CriarTabelaObra()
CriarTabelaFuncionario()


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

@app.route("/Banco")
def Banco():
    pessoas = get_data()
    return render_template("Banco.html", pessoas=pessoas)

@app.route("/Adicionador")
def BancoObraOO():
    Obra = BancoObra()
    Funcionario = BancoFuncionario()
    return render_template("Adicionador.html", Obra=Obra, Funcionario=Funcionario)

#Acessando funções

@app.route("/Add", methods=["POST"])
def Adicionar():
    return add()

@app.route("/Delete", methods=["POST"])
def Deletando():
    return delete()

@app.route("/Confirmacao", methods=["POST"])
def confirmar_usuario():
    return Confirmacao()

@app.route("/AddObra", methods=["POST"])
def OOAddObra():
    return AddObra()

@app.route("/DeleteObra", methods=["POST"])
def OODeleteObra():
    return DeleteObra()

@app.route("/AddFuncionario", methods=["POST"])
def OOAddFuncionario():
    return AddFuncionario()

@app.route("/DeleteFuncionario", methods=["POST"])
def OODeleteFuncionario():
    return DeleteFuncionario()



# colocar o site no ar

if __name__ == "__main__":
    #webview.start()
    app.run(debug=True)
    
