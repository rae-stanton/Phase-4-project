import os
from flask_cors import CORS
from flask import Flask, make_response, jsonify, request
from flask_migrate import Migrate
from flask_restful import Resource, Api
# assuming models.py is in the same directory
from server.models import User, Product, db
from flask_bcrypt import Bcrypt

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DATABASE = os.environ.get(
    "DB_URI", f"sqlite:///{os.path.join(BASE_DIR, 'shoppingapp.db')}"
)

bcrypt = Bcrypt()
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)
migrate = Migrate(app, db)
bcrypt.init_app(app)

api = Api(app)
CORS(app)


@app.route("/")
def home():
    return "Welcome to the Shopping App!"


class Users(Resource):
    def get(self):
        # Fetch all users from the database
        users = User.query.all()

        # Convert each user to dictionary format and return as a list
        return jsonify({"users": [user.to_dict() for user in users]})

    def post(self):
        # Parsing the request data
        data = request.get_json()

        # Validating the necessary fields
        if not data.get('name') or not data.get('email') or not data.get('password'):
            return {"message": "Name, Email, and Password are required!"}, 400

        # Check if user already exists using the provided email
        existing_user = User.query.filter_by(email=data['email']).first()
        if existing_user:
            return {"message": "A user with this email already exists."}, 400

        # Create a new user instance
        user = User(name=data['name'], email=data['email'])

        # Use the set_password method to hash and set the user's password
        user.set_password(data['password'])

        # Add the user to the database session and commit to save the new user to the database
        db.session.add(user)
        db.session.commit()

        # Return a success message and the newly created user's details
        return {"message": "User created successfully!", "user": {"id": user.id, "name": user.name, "email": user.email}}, 201


api.add_resource(Users, "/users")

if __name__ == "__main__":
    app.run(port=5000, debug=True)
