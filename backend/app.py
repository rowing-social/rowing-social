from flask import Flask, jsonify, request
from models import db, User, Session
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
    user = user.to_dict(sessions=True)
    return jsonify(user)

##############
## Sessions ##
##############

@app.route("/sessions", methods=['GET'])
def get_sessions():
    sessions = Session.query.all()
    sessions = [x.to_dict() for x in sessions]
    return jsonify(sessions)


@app.route("/sessions", methods=['POST'])
def post_sessions():
    data = request.get_json()
    try:
        datetime = data['datetime']
        distance = data['distance']
        user_id = data['user_id']
        user = User.query.filter_by(id=user_id).first_or_404()
    except:
        return jsonify({'success': False}), 400
    session = Session(
        user_id = user.id,
        distance = distance,
        datetime = datetime,
        kcal = data.get('kcal', None),
        strokerate = data.get('strokerate', None),
        duration = data.get('duration', None),
        intensity = data.get('intensity', None)
    )

    try:
        db.session.add(session)
        db.session.commit()
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({"success": False}), 420
    return jsonify({"success": True}), 201
