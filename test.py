

from flask import Flask, request
app = Flask(__name__)
@app.route('/coucou')
def dire_coucou():
    return 'Coucou !'
if __name__ == '__main__':
   app.run()

