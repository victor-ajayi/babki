import os

from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))

load_dotenv()

DB_PASS = os.environ.get("DB_PASS")


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = f"postgresql://postgres:{DB_PASS}@localhost/babki"

    SQLALCHEMY_TRACK_MODIFICATIONS = False
