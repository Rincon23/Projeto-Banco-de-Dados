import sqlite3

try:
    #Conectando no banco
    banco = sqlite3.connect('primeiro_banco.db')

    cursor = banco.cursor()

    cursor.execute("DELETE from pessoas WHERE idade = 21")

    banco.commit() 
    banco.close()
    print("Os dados foram removidos")

except sqlite3.Error as erro:
    print("Erro ao excluir: ", erro)