import sqlite3

#Conectando no banco
banco = sqlite3.connect('primeiro_banco.db')

cursor = banco.cursor()

#Criar tabela (Apenas 1 vez)
cursor.execute("CREATE TABLE pessoas (nome text,idade integer, objeto text)")
