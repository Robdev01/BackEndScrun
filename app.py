from flask import Flask, request, jsonify
from werkzeug.security import generate_password_hash
from banco import inserir_usuario, buscar_usuario_por_email, check_password_hash

app = Flask(__name__)

@app.route('/register', methods=['POST'])
def registrar_usuario():
    data = request.get_json()

    nome = data.get('nome')
    email = data.get('email')
    senha = data.get('senha')
    tipo = data.get('tipo')

    if tipo not in ['admin', 'desenvolvedor']:
        return jsonify({'erro': 'Tipo inválido. Use "admin" ou "desenvolvedor".'}), 400

    if not all([nome, email, senha, tipo]):
        return jsonify({'erro': 'Todos os campos são obrigatórios'}), 400

    senha_hash = generate_password_hash(senha)

    sucesso, mensagem = inserir_usuario(nome, email, senha_hash, tipo)
    
    if sucesso:
        return jsonify({'mensagem': mensagem}), 201
    else:
        return jsonify({'erro': mensagem}), 400


@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    senha = data.get('senha')

    if not all([email, senha]):
        return jsonify({'erro': 'Email e senha são obrigatórios'}), 400

    usuario = buscar_usuario_por_email(email)
    
    if not usuario:
        return jsonify({'erro': 'Usuário não encontrado'}), 404

    id, nome, email_db, senha_db, tipo = usuario

    if not check_password_hash(senha_db, senha):
        return jsonify({'erro': 'Senha incorreta'}), 401

    return jsonify({
        'mensagem': f'Login bem-sucedido. Bem-vindo, {nome}!',
        'tipo': tipo
    }), 200

if __name__ == "__main__":
    app.run(debug=True)
