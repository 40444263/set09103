from flask import *
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello Napier"

@app.route('/static-example/img')
def static_example_img():
    start = '<img src="../img'
    url = url_for('static',filename='vmask.jpg')
    end = '">'
    return start + url + end

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
