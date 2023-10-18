from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Declare the extensions outside the function, but don't initialize them yet
db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///shoppingapp.db'

    # Initialize the extensions with the app inside the function
    db.init_app(app)
    migrate.init_app(app, db)

    # Import models to ensure they're attached to the SQLAlchemy instance
    from . import models

    return app
