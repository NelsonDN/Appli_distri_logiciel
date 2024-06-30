
from . import schema as sch


DEMO_USERS = [
    dict(mail='jean@yahoo.com',
        password=hash('demo'),
        nom='Jean',
        prenom='Honji',
        tel=75555555,
        type='D'),
    dict(mail='lucie@yahoo.com',
        password=hash('demo'),
        nom='Lucie',
        prenom='Honja',
        tel=75555555,
        type='D'),
    dict(mail='marc@yahoo.com',
        password=hash('demo'),
        nom='Marc',
        prenom='Honz',
        tel=7555855,
        type='C')
]

DEMO_TOOLS = [
    dict(nom='thematic_analysis',
         desc="outils d'analyse thematique",
         version='1.0',
         payant=True, 
         auteur='jean@yahoo.com'),
    dict(nom='content_analysis',
        desc="outils d'analyse de contenu",
        version='1.0',
        payant=True, 
        auteur='jean@yahoo.com'),
    dict(nom='narrative_analysis',
        desc="outils d'analyse narrative",
        version='1.0',
        payant=False, 
        auteur='lucie@yahoo.com'),
    dict(nom='grounded_theory',
        desc="outils theorrie ancree",
        version='2.0',
        payant=False, 
        auteur='jean@yahoo.com')
]

def create_data(session):
    query = session.query(sch.Utilisateur)
    # users = {user.mail:user for user in query.all()}
    # query = session.query(sch.Composant)
    # tools = {tool.nom:tool for tool in query.all()}
    # print(users)
    # print(tools)
    
    # for row in DEMO_USERS:
    #     if row['mail'] not in users:
    #         user = sch.Utilisateur(**row)
    #         session.add(user)
    #         users[user.mail] = user
    # for row in DEMO_TOOLS:
    #     if row['nom'] not in tools:
    #         auteur = row.pop("auteur")
    #         tool = sch.Composant(**row)
    #         tool.user = users[auteur]
    #         session.add(tool)
    # session.commit()
    
    