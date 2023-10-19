import os
from flask import Flask, make_response, jsonify
from flask_migrate import Migrate
from flask_restful import Resource, Api
from .models import User, db  # assuming models.py is in the same directory

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DATABASE = os.environ.get(
    "DB_URI", f"sqlite:///{os.path.join(BASE_DIR, 'shoppingapp.db')}"
)

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)
migrate = Migrate(app, db)


api = Api(app)


@app.route("/")
def home():
    return "Welcome to the Shopping App!"


class Users(Resource):
    def get(self):
        users = User.query.all()
        # This will print users to the terminal to see if the query is fetching them correctly
        print(users)
        return jsonify({"users": [user.to_dict() for user in users]})


api.add_resource(Users, "/users")

if __name__ == "__main__":
    app.run(port=5000, debug=True)
