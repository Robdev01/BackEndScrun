from flask import request, jsonify
from banco import get_db_connection
from werkzeug.security import generate_password_hash, check_password_hash
from models import User

def init_routes(app):
      @app.route('/login', methods=['POST'])
      def login():
          data = request.get_json()
          email = data.get('email')
          password = data.get('password')

          if not email or not password:
              return jsonify({'message': 'Por favor, preencha todos os campos'}), 400

          conn = get_db_connection()
          cursor = conn.cursor()
          cursor.execute('SELECT * FROM users WHERE email = ?', (email,))
          user_data = cursor.fetchone()

          if user_data and check_password_hash(user_data['password'], password):
              user = User(user_data['id'], user_data['email'], user_data['password'], user_data['name'])
              return jsonify({
                  'message': 'Login bem-sucedido',
                  'user': {
                      'id': user.id,
                      'email': user.email,
                      'name': user.name
                  }
              }), 200

          conn.close()
          return jsonify({'message': 'Email ou senha incorretos'}), 401

      @app.route('/register', methods=['POST'])
      def register():
          data = request.get_json()
          email = data.get('email')
          password = data.get('password')
          name = data.get('name')

          if not email or not password or not name:
              return jsonify({'message': 'Todos os campos são obrigatórios'}), 400

          conn = get_db_connection()
          cursor = conn.cursor()
          cursor.execute('SELECT * FROM users WHERE email = ?', (email,))
          if cursor.fetchone():
              conn.close()
              return jsonify({'message': 'Email já registrado'}), 400

          hashed_password = generate_password_hash(password)
          cursor.execute('INSERT INTO users (email, password, name) VALUES (?, ?, ?)',
                        (email, hashed_password, name))
          conn.commit()
          conn.close()

          return jsonify({'message': 'Usuário registrado com sucesso'}), 201