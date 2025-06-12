# API de Gestão de Tarefas (Flask)

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

├── app.py # Ponto de entrada da aplicação
├── banco.py # Conexão e inicialização do banco SQLite
├── criar_banco.py # Script para criar o banco manualmente
├── models.py # Classes modelo (User, Task)
├── routes.py # Definição das rotas da API
├── requisition.txt # (Opcional) Exemplos de requisições
├── Procfile # Para deploy no Heroku
└── README.md # Documentação do projeto

bash
Copiar
Editar

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
bash
Copiar
Editar
python app.py
A aplicação estará disponível em: http://localhost:8080

```

##📝 Exemplos de Requisição
Registro
json
Copiar
Editar
POST /register
{
  "email": "exemplo@email.com",
  "password": "123456",
  "name": "Usuário Teste"
}
Login
json
Copiar
Editar
POST /login
{
  "email": "exemplo@email.com",
  "password": "123456"
}
Criar Tarefa
json
Copiar
Editar
POST /tasks
{
  "title": "Implementar API",
  "description": "Criar endpoints de tarefas",
  "assignee": "João",
  "storyPoints": 5,
  "status": "To Do"
}
🛠️ Deploy
Se desejar hospedar no Heroku, certifique-se de ter o arquivo Procfile corretamente configurado com:

makefile
Copiar
Editar
web: python app.py
E siga o processo padrão de deploy para o Heroku.

📌 Notas
Esta API não possui autenticação com tokens ou JWT. É recomendável adicionar segurança adicional em ambientes de produção.

O banco de dados é SQLite, ideal para testes e desenvolvimento local.

📬 Contato
Desenvolvido por [Seu Nome]. Contribuições e sugestões são bem-vindas!

bash
Copiar
Editar

Se quiser, posso adaptar para português/informal, ou adicionar instruções específicas para o Heroku, Docker, ou autenticação via JWT. Deseja algo mais?







