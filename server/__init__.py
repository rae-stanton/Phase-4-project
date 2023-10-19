
# from flask_migrate import Migrate
# # from flask_bcrypt import Bcrypt

# # Declare the extensions outside the function, but don't initialize them yet
# db = SQLAlchemy()
# migrate = Migrate()
# # bcrypt = Bcrypt()


# def create_app():
#     app = Flask(__name__)
#     app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///shoppingapp.db'
#     app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#     # app.config['SECRET_KEY'] = 'your_secret_key_here'

#     # Initialize the extensions with the app inside the function
#     db.init_app(app)
#     migrate.init_app(app, db)
#     # bcrypt.init_app(app)

#     # Import models to ensure they're attached to the SQLAlchemy instance
#     from . import models

#     # Register blueprints
#     from .routes import main

#     return app
