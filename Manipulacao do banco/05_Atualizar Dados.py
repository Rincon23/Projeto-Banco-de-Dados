import sqlite3

#Conectando no banco
banco = sqlite3.connect('primeiro_banco.db')

cursor = banco.cursor()

cursor.execute("UPDATE pessoas SET nome = 'Fabio' WHERE idade = 30")

banco.commit()