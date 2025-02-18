import sqlite3

nome = input("Nome: ")
idade = input("Idade: ")
objeto = input("Nome do Objeto: ")
#Conectando no banco
banco = sqlite3.connect('primeiro_banco.db')

cursor = banco.cursor()
#inserir dados
cursor.execute("INSERT INTO pessoas VALUES ('"+nome+"',"+str(idade)+",'"+objeto+"')")

banco.commit() 

