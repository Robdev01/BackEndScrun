from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)

DB_PATH = "usuarios.db"

def get_usuario_por_email(email):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT email, senha FROM usuarios WHERE email = ?", (email,))
    user = cursor.fetchone()
    conn.close()
    return user  # retorna tupla (email, senha) ou None

def criar_usuario(email, senha):
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO usuarios (email, senha) VALUES (?, ?)", (email, senha))
        conn.commit()
        conn.close()
        return True
    except sqlite3.IntegrityError:
        return False

@app.route("/api/login", methods=["POST"])
def login():
    data = request.get_json()
    email = data.get("email")
    password = data.get("password")

    user = get_usuario_por_email(email)

    if user and user[1] == password:
        return jsonify({"success": True, "message": "Login realizado com sucesso!"})
    else:
        return jsonify({"success": False, "message": "Credenciais inválidas."}), 401

@app.route("/api/register", methods=["POST"])
def register():
    data = request.get_json()
    email = data.get("email")
    password = data.get("password")

    if not email or not password:
        return jsonify({"success": False, "message": "Email e senha são obrigatórios."}), 400

    if get_usuario_por_email(email):
        return jsonify({"success": False, "message": "Usuário já existe."}), 409

    if criar_usuario(email, password):
        return jsonify({"success": True, "message": "Usuário cadastrado com sucesso!"})
    else:
        return jsonify({"success": False, "message": "Erro ao cadastrar usuário."}), 500

if __name__ == "__main__":
    app.run(debug=True)
