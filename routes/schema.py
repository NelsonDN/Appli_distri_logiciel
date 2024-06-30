from config import db

class Utilisateur(db.Model):
    
    __tablename__ = 'Utilisateurs'
    
    id = db.Column(db.Integer, primary_key=True)
    mail = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    nom = db.Column(db.String, nullable=False)
    prenom = db.Column(db.String)
    tel = db.Column(db.Integer, unique=True)
    type = db.Column(db.String(1), nullable=False) # C=Chercheur | D=Developpeur
    
    def __repr__(self):
        return f"Mail: {self.mail}, Nom: {self.nom}"

class Composant(db.Model):
    
    __tablename__ = 'Composants'
    
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String, nullable=False)
    desc = db.Column(db.String, nullable=False)
    type = db.Column(db.String, nullable=True)
    version = db.Column(db.String, nullable=False)
    payant = db.Column(db.Boolean, nullable=False)
    prix = db.Column(db.Integer, nullable=True) 
    
    id_utilisateur = db.Column(db.Integer, db.ForeignKey('Utilisateurs.id'), nullable=False)
    auteur = db.relationship('Utilisateur', backref=db.backref('composants'), lazy=True)

class Commentaire(db.Model):
    
    __tablename__ = 'Commentaires'
    
    id = db.Column(db.Integer, primary_key=True)
    contenu_com = db.Column(db.String, nullable=False)
    date_eng_com = db.Column(db.String, nullable=False)
    
    id_uti_comm = db.Column(db.Integer, db.ForeignKey('Utilisateurs.id'), nullable=False)
    uti_comm = db.relationship('Utilisateurs', backref=db.backref('commentaires_utilisateur'), lazy=True) #cle etrangere destiner a iddentifier l'utilisateur dans un commentaire

    id_comp_comm = db.Column(db.Integer, db.ForeignKey('Composants.id'), nullable=False)
    comp_comm = db.relationship('Utilisateurs', backref=db.backref('commentaires_composants'), lazy=True) #cle etrangere destiner a iddentifier le composant dans un commentaire

class Avis(db.Model):
    
    __tablename__ = 'Avis'
    
    id = db.Column(db.Integer, primary_key=True)
    note_avi = db.Column(db.String, nullable=False)
    
    id_uti_avi = db.Column(db.Integer, db.ForeignKey('Utilisateurs.id'), nullable=False)
    uti_avi = db.relationship('Utilisateurs', backref=db.backref('avis_utilisateur'), lazy=True) #cle etrangere destiner a iddentifier l'utilisateur dans un avis

    id_avis_com = db.Column(db.Integer, db.ForeignKey('Commentaires.id'), nullable=False)
    comm_avis = db.relationship('Utilisateurs', backref=db.backref('avis_commentaires'), lazy=True) #cle etrangere destiner a iddentifier le avis dans un commentaire

# class Avis(db.Model):
    
#     __tablename__ = 'Compatibilite'
    
#     id = db.Column(db.Integer, primary_key=True)
#     note_avi = db.Column(db.String, nullable=False)
    
#     id_uti_avi = db.Column(db.Integer, db.ForeignKey('Utilisateurs.id'), nullable=False)
#     uti_avi = db.relationship('Utilisateurs', backref=db.backref('avis_utilisateur'), lazy=True) #cle etrangere destiner a iddentifier l'utilisateur dans un avis

#     id_avis_com = db.Column(db.Integer, db.ForeignKey('Commentaires.id'), nullable=False)
#     comm_avis = db.relationship('Utilisateurs', backref=db.backref('avis_commentaires'), lazy=True) #cle etrangere destiner a iddentifier le avis dans un commentaire
