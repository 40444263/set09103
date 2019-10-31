from flask import Flask , session

app = Flask ( __name__ )
app.secret_key = 'A0Zr98j /3 yX R~XHH!jmN]LWX / ,? RT '

@app . route ('/')
def index () :
    return "Root route for the sessions example "

@app . route ('/session/write/<name>/')
def write(name = None ) :
    session['name'] = name
    return " Wrote %s into 'name ' key of session " % name

@app . route ('/session/read/')
def read () :
    try:
        if(session ['name']) :
            return str(session['name'])
    except KeyError:
        pass
    return "No session variable set for 'name ' key "

@app . route ('/ session / remove /')
def remove () :
    session . pop ('name ', None )
    return " Removed key 'name ' from session "

<<<<<<< HEAD
if __name__ == " __main__ ":
    app.run(host ='0.0.0.0 ', debug = True )
=======
if __name__ == "__main__":
    print "ici"
    init(app)
    app.run(host = app.config['ip_address'],port= int(app.config['port']))
>>>>>>> 2f914bf3528f814bc41e4ea71ff8bb6929b0d6c2
