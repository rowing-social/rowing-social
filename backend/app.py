from flask import Flask, jsonify, request
from models import db, User
from sqlalchemy.exc import SQLAlchemyError

app = Flask(__name__)
app.config.from_object("config.Config")
app.app_context().push()
db.init_app(app)
db.create_all()

@app.route("/")
def hello_world():
    return "Hello, World!"

###########
## Users ##
###########

@app.route("/users", methods=['GET'])
def get_users():
    users = User.query.all()
    users = [x.to_dict() for x in users]
    return jsonify(users)

@app.route("/users", methods=['POST'])
def post_users():
    data = request.get_json()
    try:
        name = data['name']
        email = data['email']
    except:
        return jsonify({'success': False}), 400
    user = User(name=name, email=email)

    try:
        db.session.add(user)
        db.session.commit()
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({"success": False}), 420
    return jsonify({"success": True}), 201

@app.route("/users/<user_id>", methods=['GET'])
def get_user_by_id(user_id):
    user = User.query.filter_by(id=user_id).first_or_404()
    user = {"id": user.id, "name": user.name, "email": user.email}
    return jsonify(user)
