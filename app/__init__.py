import os
from pathlib import PurePath

from flask import Flask
from flask_migrate import Migrate
from flask_session import Session

from config import Config

from .api import bp as api_bp
from .extensions import db

app_path = PurePath(__file__)


def create_app():
    # Configure app
    app = Flask(__name__)
    app.secret_key = os.urandom(30)
    app.config["SESSION_TYPE"] = "filesystem"
    app.config.from_object(Config)
    migrate = Migrate()
    session = Session()

    # Initialize Flask extensions
    db.init_app(app)
    migrate.init_app(app, db)
    session.init_app(app)

    # Register blueprint
    app.register_blueprint(api_bp)

    with app.app_context():
        db.create_all()

    return app
