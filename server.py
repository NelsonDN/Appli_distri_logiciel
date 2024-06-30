from config import app
from routes import *    #tres important

if __name__ == '__main__':
    app.run(debug=True)
    





# @app.route('/')
# def index():
#     return render_template('index.html')

#@app.route('/')
#@app.route('/demo')
#def demo_accueil():
 #   return render_template('demo_accueil.html')

#@app.route('/demo/outils')
#def demo_outils():
 #   return render_template('demo_outils.html')

#@app.route('/demo/details/<nom>')
#def demo_details(nom):
#    return render_template('demo_details.html')

#@app.route('/demo/telechargement/<nom>')
#def demo_telechargement(nom):
 #   return render_template('index.html')

#@app.route('/demo/achat/<nom>')
#def demo_achat(nom):
 #   return render_template('index.html')


    