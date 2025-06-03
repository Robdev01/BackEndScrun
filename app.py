from flask import Flask
from routes import init_routes
from banco import init_db
from flask_cors import CORS
import os
app = Flask(__name__)

CORS(app)
# Inicializa o banco de dados antes de iniciar o servidor
init_db()

init_routes(app)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)