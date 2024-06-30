
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import os
from werkzeug.utils import secure_filename

baseDir = os.path.dirname(__file__)
dbDir = os.path.join(baseDir, 'datas/test.db')

# configuration des constantes
DEBUG = True
SECRET_KEY = "FleuMan"
SQLALCHEMY_DATABASE_URI = "sqlite:///"+dbDir
SQLALCHEMY_TRACK_MODIFICATIONS = False

app = Flask(__name__)
app.config.from_object(__name__)

UPLOAD_FOLDER = 'uploads'  # Chemin où les fichiers seront stockés sur le serveur
ALLOWED_EXTENSIONS = {'exe'}  # Extensions autorisées pour les fichiers setup

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


# configuration de la base de données
db = SQLAlchemy()
db.init_app(app)

login_manager = LoginManager(app)
login_manager.login_view = 'login'

from schema2 import Utilisateur

@login_manager.user_loader
def load_user(user_id):
    return Utilisateur.query.get(int(user_id))