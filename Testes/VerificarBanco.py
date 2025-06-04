import sqlite3

# Conectar ao banco de dados
conn = sqlite3.connect('../scrum.db')
cursor = conn.cursor()

# Consultar as tabelas existentes
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tabelas = cursor.fetchall()

# Exibir as tabelas
print("Tabelas no banco de dados:")
for tabela in tabelas:
    print(tabela[0])

# Fechar a conexão
conn.close()