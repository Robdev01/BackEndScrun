import sqlite3

def inserir_usuario(nome, email, senha_hash, tipo):
    conn = sqlite3.connect("usuarios.db")
    cursor = conn.cursor()

    try:
        cursor.execute("""
        INSERT INTO usuarios (nome, email, senha, tipo)
        VALUES (?, ?, ?, ?)
        """, (nome, email, senha_hash, tipo))

        conn.commit()
        return True, "Usuário inserido com sucesso"
    except sqlite3.IntegrityError as e:
        return False, f"Erro ao inserir: {str(e)}"
    finally:
        conn.close()

def buscar_usuario_por_email(email):
    conn = sqlite3.connect("usuarios.db")
    cursor = conn.cursor()

    cursor.execute("""
    SELECT id, nome, email, senha, tipo FROM usuarios WHERE email = ?
    """, (email,))
    
    usuario = cursor.fetchone()
    conn.close()
    return usuario 