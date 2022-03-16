from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/hola_mundo/")
def hola():
    return "Hola mundo"


if __name__ == "__main__":
    app.run()
