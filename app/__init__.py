from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__, template_folder='../templates')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

from app import routes, models

with app.app_context():
    db.create_all()
    print("Database tables created")
