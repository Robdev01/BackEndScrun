import sqlite3

conn = sqlite3.connect("usuarios.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    email TEXT NOT NULL UNIQUE,
    senha TEXT NOT NULL
)
""")

cursor.execute("INSERT OR IGNORE INTO usuarios (email, senha) VALUES (?, ?)", ("admin@teste.com", "123456"))

conn.commit()
conn.close()
print("Banco criado e usuário inserido.")
