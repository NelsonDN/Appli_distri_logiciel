
from flask import jsonify
from flask import render_template, request, redirect, url_for, flash, send_from_directory
from config2 import app, db
from demos2 import create_data
import schema2 as sch
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
import os
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = '/uploads'  
ALLOWED_EXTENSIONS = {'exe'} 
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.before_first_request
def initialize_database():
    create_data(db.session)
    
    
@app.teardown_request
def shutdown_session(exception=None):
    db.session.remove()
    
@app.route('/')
def accueil():
    return render_template('accueil.html')

@app.route('/temp/<page>')
def temp(page):
    return page + ' en construction'

@app.route('/users')
def users():
    users = db.session.query(sch.Utilisateur).all()
    return jsonify([str(user) for user in users])

@app.route('/tools')
def tools():
    composants = db.session.query(sch.Composant).all()
    return jsonify([str(obj) for obj in composants])

@app.route('/Seconnecter')
def Seconnecter():
    return render_template('Seconnecter.html')


@app.route('/incription')
def incription():
    return render_template('inscription.html')

@app.route('/téléchargement')
def téléchargement():
    return render_template('téléchargement.html')

@app.route('/mot de passe')
def motdepasse():
    return render_template('mot de passe.html')

@app.route('/com')
def com():
    return render_template('com.html')

@app.route('/developpeur')
def developpeur():
    return render_template('developpeur.html')

@app.route('/Avis')
def Avis():
    return render_template('Avis.html')

@app.route('/confirmation')
def confirmation():
    return render_template('confirmation.html')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/outils')
def outils():
    composants = db.session.query(sch.Composant).all()
    return render_template('outils.html', composants=composants)

@app.route('/composant/<int:id>/detail', methods=['GET','POST'])
def details(id):
    composant = sch.Composant.query.get_or_404(id)
    os = sch.Os.query.filter_by(id_composant=id).first()

    return render_template('details.html', composant=composant, os=os)

@app.route('/download/<path:filename>', methods=['GET'])
@login_required
def download_setup(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename, as_attachment=True)

@app.route('/formulaire_paiement')
@login_required
def formulaire_paiement():
    return render_template('formulaire_paiement.html')

@app.route('/composant/<int:id>/commentaire', methods=['POST'])
@login_required
def ajouter_commentaire(id):
    composant = sch.Composant.query.get_or_404(id)
    contenu = request.form['contenu']
    
    commentaire = sch.Commentaire(contenu=contenu, id_utilisateur=current_user.id, id_composant=id, responsable=composant)
    db.session.add(commentaire)
    db.session.commit()
    
    flash('Votre commentaire a été ajouté avec succès.', 'success')
    return redirect(url_for('details', id=id))

@app.route('/inscrire', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        nom = request.form['nom']
        prenom = request.form['prenom']
        tel = request.form['tel']
        password = request.form['password']
        email = request.form['email']
        typeCompte = request.form['type']

        hashed_password = generate_password_hash(password)
        # is_correct_password = check_password_hash(hashed_password, entered_password)

        utilisateur = sch.Utilisateur(email=email, password=hashed_password, nom=nom, prenom=prenom, tel=tel, type=typeCompte)
        
        db.session.add(utilisateur)
  
        db.session.commit()
        
        # Redirection vers la page de connexion après l'inscription
        return redirect(url_for('Seconnecter'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        
        utilisateur = sch.Utilisateur.query.filter_by(email=email).first()
        if utilisateur and check_password_hash(utilisateur.password, password):
            login_user(utilisateur)
            return redirect(url_for('accueil'))
        
    return render_template('Seconnecter.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('accueil'))

@app.route('/composants_list')
@login_required
def composants_list():
    if 'D' != current_user.type:
        return redirect(url_for('outils'))
    composants = sch.Composant.query.filter_by(id_utilisateur=current_user.id).all()
    return render_template('composants_list.html', composants=composants)

@app.route('/composants_ajouter')
@login_required
def composants_ajouter():
    if 'D' != current_user.type:
        return redirect(url_for('outils'))
    return render_template('composants_ajouter.html')

@app.route('/ajouter', methods=['GET', 'POST'])
@login_required
def ajouter():
    if 'D' != current_user.type:
        return redirect(url_for('outils'))
    if request.method == 'POST':
        nom = request.form['nom']
        desc = request.form['desc']
        version = request.form['version']
        icon = request.form['icon']
        payant = 'payant' in request.form
        prix = request.form.get('prix')
        nom_os = request.form['nom_os']
        version_os = request.form['version_os']

        chemin_setup = None  

        if not os.path.exists(app.config['UPLOAD_FOLDER']):
            print("paaaaaaaaaasssssssssssss")
            os.makedirs(app.config['UPLOAD_FOLDER'])

       # Gestion de l'upload du fichier setup
        if 'setup' in request.files:
            setup_file = request.files['setup']
            if setup_file.filename == '':
                flash('Aucun fichier sélectionné', 'warning')
            elif setup_file and allowed_file(setup_file.filename):
                filename = secure_filename(setup_file.filename)
                chemin_setup = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                setup_file.save(chemin_setup)
            else:
                flash('Type de fichier non autorisé', 'danger')
                return redirect(request.url)
            
        
        composant = sch.Composant(nom=nom, desc=desc, version=version, icon=icon, payant=payant, prix=prix, chemin_setup=filename)

        if current_user.is_authenticated:
            composant.id_utilisateur = current_user.id  
            composant.auteur = current_user  

        db.session.add(composant)
        db.session.commit()

        os_ = sch.Os(nom=nom_os, version=version_os)
        os_.id_composant = composant.id 
        os_.responsable = composant  

        db.session.add(os_)
        db.session.commit()



        return redirect(url_for('composants_list'))
    
    return render_template('composants_ajouter.html')

@app.route('/composant/<int:id>/editer', methods=['GET', 'POST'])
@login_required
def editer_composant(id):
    if 'D' != current_user.type:
        return redirect(url_for('outils'))
    composant = sch.Composant.query.get_or_404(id)
    os_ = sch.Os.query.filter_by(id_composant=id).first()
    print(os_)
    if request.method == 'POST':
        composant.nom = request.form['nom']
        composant.desc = request.form['desc']
        composant.version = request.form['version']
        composant.icon = request.form['icon']
        composant.payant = 'payant' in request.form
        composant.prix = request.form['prix'] if composant.payant else None
        os_.nom = request.form['nom_os']
        os_.version = request.form['version_os']

        db.session.commit()
        flash('Le composant a été mis à jour avec succès.', 'success')
        return redirect(url_for('composants_list'))
    return render_template('composants_editer.html', composant=composant, os_=os_)

@app.route('/composant/<int:id>/supprimer', methods=['POST'])
@login_required
def supprimer_composant(id):
    if 'D' != current_user.type:
        return redirect(url_for('outils'))
    composant = sch.Composant.query.get_or_404(id)

    if composant.id_utilisateur != current_user.id:
        return redirect(url_for('composants_list'))
    
    db.session.delete(composant)
    db.session.commit()
    flash('Le composant a été supprimé avec succès.', 'success')
    return redirect(url_for('composants_list'))

