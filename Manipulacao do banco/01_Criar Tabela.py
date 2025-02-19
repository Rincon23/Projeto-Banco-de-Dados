import sqlite3

# Conectando ao banco
banco = sqlite3.connect('primeiro_banco.db')
cursor = banco.cursor()

# Criar a tabela apenas se ela não existir
cursor.execute("""
CREATE TABLE IF NOT EXISTS pessoas (
    nome TEXT,
    idade INTEGER,
    objeto TEXT
)
""")

# Confirmar e fechar conexão
banco.commit()
banco.close()

