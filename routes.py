from flask import request, jsonify
from banco import get_db_connection
from werkzeug.security import generate_password_hash, check_password_hash
from models import User

def init_routes(app):
    # LOGIN
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
            conn.close()
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

    # REGISTER
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

    # CRIAR TASK
    @app.route('/tasks', methods=['POST'])
    def criar_task():
        data = request.get_json()
        title = data.get('title')
        description = data.get('description')
        assignee = data.get('assignee')
        storyPoints = data.get('storyPoints')
        status = data.get('status')

        if not title or storyPoints is None or not status:
            return jsonify({'message': 'Campos obrigatórios ausentes'}), 400

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO tasks (title, description, assignee, storyPoints, status)
            VALUES (?, ?, ?, ?, ?)
        ''', (title, description, assignee, storyPoints, status))
        conn.commit()
        conn.close()
        return jsonify({'message': 'Tarefa criada com sucesso'}), 201

    # LISTAR TASKS
    @app.route('/tasks', methods=['GET'])
    def listar_tasks():
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM tasks')
        tasks = cursor.fetchall()
        conn.close()

        resultado = []
        for row in tasks:
            resultado.append({
                'id': row['id'],
                'title': row['title'],
                'description': row['description'],
                'assignee': row['assignee'],
                'storyPoints': row['storyPoints'],
                'status': row['status']
            })
        return jsonify(resultado)

    # ATUALIZAR TASK
    @app.route('/tasks/<int:task_id>', methods=['PUT'])
    def atualizar_task(task_id):
        data = request.get_json()
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM tasks WHERE id = ?', (task_id,))
        task = cursor.fetchone()

        if not task:
            conn.close()
            return jsonify({'message': 'Tarefa não encontrada'}), 404

        cursor.execute('''
            UPDATE tasks
            SET title = ?, description = ?, assignee = ?, storyPoints = ?, status = ?
            WHERE id = ?
        ''', (
            data.get('title', task['title']),
            data.get('description', task['description']),
            data.get('assignee', task['assignee']),
            data.get('storyPoints', task['storyPoints']),
            data.get('status', task['status']),
            task_id
        ))
        conn.commit()
        conn.close()
        return jsonify({'message': 'Tarefa atualizada com sucesso'})

    # DELETAR TASK
    @app.route('/tasks/<int:task_id>', methods=['DELETE'])
    def deletar_task(task_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM tasks WHERE id = ?', (task_id,))
        task = cursor.fetchone()

        if not task:
            conn.close()
            return jsonify({'message': 'Tarefa não encontrada'}), 404

        cursor.execute('DELETE FROM tasks WHERE id = ?', (task_id,))
        conn.commit()
        conn.close()
        return jsonify({'message': 'Tarefa deletada com sucesso'})
