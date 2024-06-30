import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# file path
baseDir = os.path.dirname(__file__)
dbDir = os.path.join(baseDir, 'datas/datas.db')

# configuration des constantes
DEBUG = True
SECRET_KEY = "FleuMan"
SQLALCHEMY_DATABASE_URI = "sqlite:///"+dbDir
SQLALCHEMY_TRACK_MODIFICATIONS = False

app = Flask(__name__)
app.config.from_object(__name__)

# configuration de la base de données
db = SQLAlchemy()
db.init_app(app)
Migrate(app, db)

