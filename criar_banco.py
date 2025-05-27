# criar_banco.py
import sqlite3

conn = sqlite3.connect("usuarios.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    senha TEXT NOT NULL,
    tipo TEXT NOT NULL  -- Ex: 'admin' ou 'desenvolvedor'
)
""")

conn.commit()
conn.close()
print("Banco criado com sucesso usando sqlite3!")
