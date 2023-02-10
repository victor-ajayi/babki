import os

from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))

load_dotenv()


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY")
    # SQLALCHEMY_DATABASE_URI = (
    #     os.environ.get(
    #         "DATABASE_URI"
    #         # ) or "sqlite:///" + os.path.join(basedir, "babki.db")
    #     )
    SQLALCHEMY_DATABASE_URI = (
        os.environ.get("DATABASE_URI")
        or "postgresql://postgres:" + os.environ.get("DB_PASS") + "@localhost/babki"
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False
