import os

USER = os.environ["POSTGRES_USER"]
PASSWORD = os.environ["POSTGRES_PASSWORD"]
HOST = os.environ["POSTGRES_HOST"]
PORT = os.environ["POSTGRES_PORT"]
DB = os.environ["POSTGRES_DB"]

class Config:
    DEBUG = True
    SECRET_KEY = "secret"
    SQLALCHEMY_DATABASE_URI = f"postgresql+psycopg2://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
