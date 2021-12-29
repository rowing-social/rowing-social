from flask import Flask

class Config:
    DEBUG = True
    SECRET_KEY = "secret"

app = Flask(__name__)
app.config.from_object("app.Config")

@app.route("/")
def hello_world():
    return "Hello, World!"
