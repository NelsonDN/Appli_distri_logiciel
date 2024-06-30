

import os
from config2 import app, dbDir
from routes2 import *
import schema2 as sch


DEMO_USERS = [
    dict(email='jean@yahoo.com',
        password=hash('demo'),
        nom='Jean',
        prenom='Honji',
        tel=75555555,
        type='D'),
    dict(email='lucie@yahoo.com',
        password=hash('demo'),
        nom='Lucie',
        prenom='Honja',
        tel=75555557,
        type='D'),
    dict(email='marc@yahoo.com',
        password=hash('demo'),
        nom='Marc',
        prenom='Honz',
        tel=7555855,
        type='C')
]

DEMO_TOOLS = [
    dict(nom='thematic_analysis',
        icon='bx bx-building',
         desc="outils d'analyse thematique",
         version='1.0',
         payant=True, 
         auteur='jean@yahoo.com', 
         chemin_setup="httrack-3.49.2.exe"),
    dict(nom='content_analysis',
        desc="outils d'analyse de contenu",
        icon='bx bx-bell',
        version='1.0',
        payant=True, 
        auteur='jean@yahoo.com', 
         chemin_setup="httrack-3.49.2.exe"),
    dict(nom='narrative_analysis',
         icon='bx bx-aperture',
        desc="outils d'analyse narrative",
        version='1.0',
        payant=False, 
        auteur='lucie@yahoo.com', 
         chemin_setup="httrack-3.49.2.exe"),
    dict(nom='grounded_theory',
         icon='bx bx-basketball',
        desc="outils theorrie ancree",
        version='2.0',
        payant=False, 
        auteur='jean@yahoo.com', 
         chemin_setup="httrack-3.49.2.exe")
]

def create_data(session):
    query = session.query(sch.Utilisateur)
    users = {user.email:user for user in query.all()}
    query = session.query(sch.Composant)
    tools = {tool.nom:tool for tool in query.all()}
    print(users)
    print(tools)
    
    for row in DEMO_USERS:
        if row['email'] not in users:
            user = sch.Utilisateur(**row)
            session.add(user)
            users[user.email] = user
    for row in DEMO_TOOLS:
        if row['nom'] not in tools:
            auteur = row.pop("auteur")
            tool = sch.Composant(**row)
            tool.user = users[auteur]
            session.add(tool)
    session.commit()


if __name__ == '__main__':
    if os.path.isfile(dbDir):
        os.unlink(dbDir)
    app.run(debug=True)
    