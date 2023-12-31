from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

db = SQLAlchemy(app)  # Movido para cima para estar disponível para importações

# Após as importações, crie as tabelas no banco de dados
with app.app_context():
    db.create_all()

from app import routes