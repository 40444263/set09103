from flask import * 
app = Flask(__name__)
@app.route("/")
def root():
    return "The default, 'root' route"

@app.route("/hello/")
def hello():
    return "Hello Napier!!!"

@app.route("/greg/")
def greg():
    return "My name is greg"

@app.route("/private")
def private():
    return redirect(url_for('greg'))
if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
