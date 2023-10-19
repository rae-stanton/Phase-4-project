import os
from flask_cors import CORS
from flask import Flask, make_response, jsonify, request
from flask_migrate import Migrate
from flask_restful import Resource, Api
# assuming models.py is in the same directory
from models import User, Product, db


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
CORS(app)


@app.route("/")
def home():
    return "Welcome to the Shopping App!"


class Users(Resource):
    def get(self):
        users = User.query.all()
        # This will print users to the terminal to see if the query is fetching them correctly
        print(users)
        return jsonify({"users": [user.to_dict() for user in users]})

    def post(self):
        # Parsing the request data
        data = request.get_json()

        # Validating the necessary fields
        if not data.get('name') or not data.get('email'):
            return {"message": "Name and Email are required!"}, 400

        # Check if user already exists
        existing_user = User.query.filter_by(email=data['email']).first()
        if existing_user:
            return {"message": "A user with this email already exists."}, 400

        # Create a new user instance and add to database
        user = User(name=data['name'], email=data['email'])
        db.session.add(user)
        db.session.commit()

        return {"message": "User created successfully!", "user": {"id": user.id, "name": user.name, "email": user.email}}, 201


class Products(Resource):
    def get(self):
        products = Product.query.all()
        # This will print products to the terminal to see if the query is fetching them correctly
        print(products)
        return jsonify({"products": [product.to_dict() for product in products]})

    def post(self):
        # Parsing the request data
        data = request.get_json()

        # Validating the necessary fields
        if not data.get('name') or not data.get('price') or not data.get('count'):
            return {"message": "Name, Price, and Count are required!"}, 400

        # Check if product already exists
        existing_product = Product.query.filter_by(name=data['name']).first()
        if existing_product:
            return {"message": "A product with this name already exists."}, 400

        # Create a new product instance and add to database
        product = Product(name=data['name'],
                          price=data['email'], count=data['count'])
        db.session.add(product)
        db.session.commit()

        return {"message": "Product created successfully!", "product": {"id": product.id, "name": product.name, "price": product.price, "count": product.count}}, 201


api.add_resource(Users, "/users")
api.add_resource(Products, "/products")

if __name__ == "__main__":
    app.run(port=5000, debug=True)
