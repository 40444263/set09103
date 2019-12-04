from flask import *
import sqlite3
from sqlite3 import *
import shutil
import json
app = Flask(__name__)

@app.route("/")
def root():
    return redirect(url_for('home'))

@app.route("/home")
def home():
    id = request.args.get('id','')
    print("fdoifko",id)
    if (id != ""):
        connexion = sqlite3.connect("static/game.db")
        curseur = connexion.cursor()
        data = curseur.execute("SELECT \"Path picture\" from Map where id =" + id +";")
        for row in data:
            print(row[0])
            shutil.copy(row[0],"static/background.jpg")
        connexion.close()
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
                'path':row[2],
                'id':row[0]
            }
        table.append(ligne)
    connexion.close()

    return render_template("map.html",table=table)

@app.route("/commands")
def commands():
    return "Commands a faire"

@app.route("/characters")
def characters():
    return render_template("characters.html")

@app.route("/game/endgame",methods =['POST','GET'])
def endgame():
    if (request.methode == "POST"):
        print("ko1")
    return "ok"





if __name__ == " __main__ ":
    app.run ( host ='0.0.0.0 ', debug = True )
