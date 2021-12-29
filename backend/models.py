import flask_sqlalchemy as fsq
import uuid
from sqlalchemy.dialects.postgresql import UUID

db = fsq.SQLAlchemy()

class Users(db.Model):
    __tablename__ = "users"
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    email = db.Column(db.String(120), unique=True, nullable=False)
