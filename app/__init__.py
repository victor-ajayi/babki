from flask import Flask
from flask_migrate import Migrate

from config import Config

from .api import bp as api_bp
from .extensions import db


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    migrate = Migrate()

    # Initialize Flask extensions
    db.init_app(app)
    migrate.init_app(app, db)

    # Register blueprint
    app.register_blueprint(api_bp)

    with app.app_context():
        db.create_all()

    return app
