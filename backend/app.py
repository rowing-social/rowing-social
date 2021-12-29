from flask import Flask
from models import db

app = Flask(__name__)
app.config.from_object("config.Config")
app.app_context().push()
db.init_app(app)
db.create_all()

@app.route("/")
def hello_world():
    return "Hello, World!"
