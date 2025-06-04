import sqlite3

# Conectar ao banco de dados
conn = sqlite3.connect('../scrum.db')
cursor = conn.cursor()

# Consultar a estrutura da tabela tasks
cursor.execute("PRAGMA table_info(tasks);")
colunas = cursor.fetchall()

# Exibir as colunas
print("Colunas da tabela tasks:")
for coluna in colunas:
    print(f"Nome: {coluna[1]}, Tipo: {coluna[2]}, Not Null: {coluna[3]}, Default: {coluna[4]}, Primary Key: {coluna[5]}")

# Fechar a conexão
conn.close()