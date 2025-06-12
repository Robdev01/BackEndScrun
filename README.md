# API para o Simulador Scrum

Este é um projeto de API REST simples desenvolvida com **Flask** e **SQLite**, que permite o registro de usuários, login e o gerenciamento de tarefas com autenticação básica.

## 🧩 Funcionalidades

- Registro de usuários (`/register`)
- Login de usuários (`/login`)
- CRUD de tarefas:
  - Criar tarefa (`POST /tasks`)
  - Listar tarefas (`GET /tasks`)
  - Atualizar tarefa (`PUT /tasks/<id>`)
  - Deletar tarefa (`DELETE /tasks/<id>`)

## 🚀 Tecnologias Utilizadas

- Python 3.x
- Flask
- SQLite
- Flask-CORS
- Werkzeug (para hash de senha)

## 📁 Estrutura de Arquivos

```
├── app.py # Ponto de entrada da aplicação
├── banco.py # Conexão e inicialização do banco SQLite
├── criar_banco.py # Script para criar o banco manualmente
├── models.py # Classes modelo (User, Task)
├── routes.py # Definição das rotas da API
├── requisition.txt # (Opcional) Exemplos de requisições
├── Procfile # Para deploy 
└── README.md # Documentação do projeto
```

## 🔧 Como executar
```
1. Clone o repositório

git clone https://github.com/seuusuario/nome-do-repo.git
cd nome-do-repo

2. Crie um ambiente virtual (opcional)

python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows

3. Instale as dependências

pip install -r requisition.txt

4. Inicialize o banco de dados

python criar_banco.py

5. Execute o servidor

python app.py
A aplicação estará disponível em: http://localhost:8080

```

## 📬 Contato
Desenvolvido por Robson Calheira. Contribuições e sugestões são bem-vindas!

Se quiser, posso adaptar para português/informal, ou adicionar instruções específicas para o Heroku, Docker, ou autenticação via JWT. Deseja algo mais?







