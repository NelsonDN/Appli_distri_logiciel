from sqlalchemy.exc import IntegrityError
from flask import render_template, request, redirect, url_for, jsonify
from config import app, db
from routes.demos import create_data
from routes import schema as sch

@app.before_request
def initialize_database():
    pass
    # create_data(db.session)
    # db.create_all()
    
    
@app.teardown_request
def shutdown_session(exception=None):
    db.session.remove()


@app.route('/users')
def get_users():
    #users = db.session.query(sch.Utilisateur).all()
    return 'Hello'
    return str(users)

@app.route('/', methods=['GET', 'POST'])
def accueil():
    return 'Hello'
    # rep1 = db.session.query(Utilisateurs).all() # .first() | .one()
    # rep2 = db.session.query(Utilisateurs).filter_by(id=1)
    if request.method == 'POST':
        print("je suis entrain de recevoir une valeur")
    # insertion
    #try:
    #     uti1 = Utilisateurs(mail_uti = 'admin@gmail.com', password_uti = 'default', nom_uti = 'Admin', prenom_uti = 'Default', tel_uti = '1234567', type_uti = 'Chercheur')
    #     db.session.add(uti1)
    #     # db.session.commit()
        
    #     uti2 = Utilisateurs(mail_uti = 'fleuro.com', password_uti = 'default', nom_uti = 'fleuro', prenom_uti = 'Default', tel_uti = '456987', type_uti = 'Chercheur')
    #     db.session.add(uti2)
    #     print("insertion effectuée avec succes!")
    # except: 
    #     print("donnees mauvaises ou existantes")
    
    #db.session.commit()
    # selection
    res = db.session.query(sch.Utilisateur)
    print(res.all())
    print("il y'a ", len(res.all())," Utilisateurs")
    return render_template('accueil.html')


@app.route('/Seconnecter')
def Seconnecter():
    return render_template('Seconnecter.html')


@app.route('/incription')
def incription():
    return render_template('inscription.html')

@app.route('/inscrire', methods=['GET', 'POST'])
def inscrire():
    print('test inscrire') 
    if request.method == 'POST':
        nom = request.form['name']
        prenom = request.form['surname']
        tel = request.form['num_tel']
        password = request.form['mot_passe']
        email = request.form['email']
        typeCompte = request.form['type_cpt']
        utilisateur = sch.Utilisateur(mail_uti=email,password_uti=password,nom_uti=nom,prenom_uti=prenom,tel_uti=tel,type_uti=typeCompte)
        db.session.add(utilisateur)
        db.session.commit()
        print(f"nom: {nom} prenom: {prenom} tel: {tel} password: {password} email: {email} typeCompte: {typeCompte}")
        res = db.session.query(sch.Utilisateur)
        print(res.all())
        print("il y'a ", len(res.all())," Utilisateurs")
    return redirect(url_for('Seconnecter'))


@app.route('/outils')
def outils():
    return render_template('outils.html')

@app.route('/details')
def details():
    return render_template('details.html')

@app.route('/téléchargement')
def téléchargement():
    return render_template('téléchargement.html')

@app.route('/test')
def test():
    return render_template('téléchargement.html')


@app.route('/mot de passe')
def motdepasse():
    return render_template('mot de passe.html')


@app.route('/com')
def com():
    return render_template('com.html')

@app.route('/Avis')
def Avis():
    return render_template('Avis.html')

@app.route('/confirmation')
def confirmation():
    return render_template('confirmation.html')


@app.route('/temp/<page>')
def temp(page):
    return page + ' en construction'

@app.route('/goodbye')
def test():
    return 'Au revoir'

@app.route('/goodbye/<name>')
def test2(name):
    return 'Au revoir ' + name