from flask import Flask
from config import Config
from .database import db, migrate
from .main import main
from .models import *


def create_app():
    # Instanciate the flask app
    app = Flask(__name__)

    # Setting app to match the config
    app.config.from_object(Config)

    # Init the database and migration
    db.init_app(app)
    migrate.init_app(app, db)

    # Registering blueprints
    app.register_blueprint(main)

    return app
