from flask import *
import sqlite3
from sqlite3 import *
app = Flask(__name__)

@app.route("/")
def root():
    return redirect(url_for('home'))

@app.route("/home")
def home():
    return render_template("home.html")


@app.route("/play")
def play():
    return render_template("game.html")


@app.route("/map")
def map():
    connexion = sqlite3.connect("static/game.db")
    curseur = connexion.cursor()
    data = curseur.execute("SELECT * from Map;")
    table = []
    for row in data:
        ligne = {
                'name': row[1],
                'nbuse':row[3],
                'path':row[2]
            }
        table.append(ligne)

    return render_template("map.html",table=table)

@app.route("/commands")
def commands():
    return "Commands a faire"

@app.route("/characters")
def characters():
    return "characters a faire"
if __name__ == " __main__ ":
    app.run ( host ='0.0.0.0 ', debug = True )
