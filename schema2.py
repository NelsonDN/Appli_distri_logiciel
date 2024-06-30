
from config2 import app, db
from sqlalchemy.sql import func
from flask_login import UserMixin

# Table d'association
avis_table = db.Table('avis',
    db.Column('utilisateur_id', db.Integer, db.ForeignKey('utilisateurs.id'), primary_key=True),
    db.Column('composant_id', db.Integer, db.ForeignKey('composants.id'), primary_key=True),
    db.Column('note', db.Integer, nullable=False),
    db.Column('commentaire', db.String, nullable=True)
)

class Utilisateur(UserMixin, db.Model):
    
    __tablename__ = 'utilisateurs'
    
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    nom = db.Column(db.String, nullable=False)
    prenom = db.Column(db.String)
    tel = db.Column(db.Integer, unique=True)
    type = db.Column(db.String(1), nullable=False) # C=Chercheur | D=Developpeur
    created_at = db.Column(db.DateTime(timezone=True),
                           server_default=func.now())
    
    def __repr__(self):
        return f"Mail: {self.email}, Nom: {self.nom}"

class Composant(db.Model):
    
    __tablename__ = 'composants'
    
    id = db.Column(db.Integer, primary_key=True)
    icon = db.Column(db.String, nullable=False)
    nom = db.Column(db.String, nullable=False)
    desc = db.Column(db.Text, nullable=False)
    type = db.Column(db.String, nullable=True)
    version = db.Column(db.String, nullable=False)
    payant = db.Column(db.Boolean, nullable=False)
    prix = db.Column(db.Integer, nullable=True) 
    created_at = db.Column(db.DateTime(timezone=True),
                           server_default=func.now())
    chemin_setup = db.Column(db.String, nullable=True)
    
    # Relation many-to-many avec Utilisateurs via la table d'association Avis
    utilisateurs = db.relationship('Utilisateur', secondary=avis_table, backref=db.backref('composants_avis', lazy='dynamic'))
    
    id_utilisateur = db.Column(db.Integer, db.ForeignKey('utilisateurs.id'))
    auteur = db.relationship('Utilisateur', backref=db.backref('composants'), lazy=True)

class Os(db.Model):
    __tablename__ = 'os'
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String, nullable=False)
    version = db.Column(db.String, nullable=True)
    id_composant = db.Column(db.Integer, db.ForeignKey('composants.id'))
    responsable = db.relationship('Composant', backref=db.backref('os'), lazy=True)

class Commentaire(db.Model):
    __tablename__ = 'commentaires'
    id = db.Column(db.Integer, primary_key=True)
    contenu = db.Column(db.String, nullable=False)
    created_at = db.Column(db.DateTime(timezone=True),
                           server_default=func.now())
    id_utilisateur = db.Column(db.Integer, db.ForeignKey('utilisateurs.id'))
    id_composant = db.Column(db.Integer, db.ForeignKey('composants.id'))
    responsable = db.relationship('Composant', backref=db.backref('commentaires_composant'), lazy=True)
    utilisateur = db.relationship('Utilisateur', backref=db.backref('commentaires_utilisateur', lazy=True))

with app.app_context():
    # db.drop_all()
    db.create_all()
    
    