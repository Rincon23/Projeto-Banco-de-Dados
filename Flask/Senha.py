from flask import Flask, request, redirect, url_for


app = Flask(__name__)


username = "admin"
password = "admin"

@app.route("/Confirmacao", methods=["POST"])
def Confirmacao():
    nomedeusuario = request.form["nomedeusuario"]
    senhadeusuario = request.form["senhadeusuario"]

    verificarlogin = False

    if nomedeusuario == username and senhadeusuario == password:
            verificarlogin = True

    if verificarlogin == True:
        print ("Login bem sucedido")
        return redirect(url_for("VisualizacaoBanco"))  # Redireciona para a página inicial
           
    else:
        print ("Login mal sucedido")
        return redirect(url_for("homepage"))   