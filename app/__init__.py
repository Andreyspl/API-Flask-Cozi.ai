from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

db = SQLAlchemy(app)  # Movido para cima para estar disponível para importações

from app import routes

# Após as importações, crie as tabelas no banco de dados
db.create_all()
