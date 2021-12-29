import flask_sqlalchemy as fsq
import uuid
from sqlalchemy.dialects.postgresql import UUID

db = fsq.SQLAlchemy()

membership = db.Table('membership',
    db.Column('user_id', UUID(as_uuid=True), db.ForeignKey('user.id'), primary_key=True),
    db.Column('team_id', UUID(as_uuid=True), db.ForeignKey('team.id'), primary_key=True)
)

class User(db.Model):
    __tablename__ = "user"
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    email = db.Column(db.String(120), unique=True, nullable=False)
    name = db.Column(db.String(50), unique=True, nullable=False)  # unique?
    sessions = db.relationship('Session', backref='User', lazy=True)
    teams = db.relationship('Team', secondary=membership, lazy='subquery',
                backref=db.backref('users', lazy=True))

class Session(db.Model):
    __tablename__ = "session"
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = db.Column(UUID(as_uuid=True), db.ForeignKey('user.id'), nullable=False)
    distance = db.Column(db.Float, nullable=False)
    datetime = db.Column(db.DateTime, nullable=False)
    kcal = db.Column(db.Integer, nullable=True)
    strokerate = db.Column(db.Float, nullable=True)
    duration = db.Column(db.Float, nullable=True)
    intensity = db.Column(db.Float, nullable=True)

class Team(db.Model):
    __tablename__ = "team"
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = db.Column(db.String(50), nullable=False)
    color = db.Column(db.String(50), nullable=False)
    goal_distance = db.Column(db.Integer, nullable=False)
    goal_date = db.Column(db.DateTime, nullable=False)
    # flag_id = db.Column(db.Integer, nullable=False)
