import os
from flask_cors import CORS
from flask import Flask, make_response, jsonify, request
from flask_migrate import Migrate
from flask_restful import Resource, Api
# assuming models.py is in the same directory
from server.models import User, Product, CartItem, db
from flask_bcrypt import Bcrypt
from flask_jwt_extended import create_access_token, JWTManager
from datetime import timedelta

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DATABASE = os.environ.get(
    "DB_URI", f"sqlite:///{os.path.join(BASE_DIR, 'shoppingapp.db')}"
)

bcrypt = Bcrypt()
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["JWT_SECRET_KEY"] = "thisisoursecretkeylol12345"
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=1)  # e.g., expires in 1 hour
db.init_app(app)
migrate = Migrate(app, db)
bcrypt.init_app(app)

api = Api(app)
CORS(app)
jwt = JWTManager(app)

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

        # Create a new product instance and add to database
        product = Product(name=data['name'],
                          price=data['email'], count=data['count'])
        db.session.add(product)
        db.session.commit()

        return {"message": "Product created successfully!", "product": {"id": product.id, "name": product.name, "price": product.price, "count": product.count}}, 201


api.add_resource(Users, "/users")
api.add_resource(Products, "/products")

class UserLogin(Resource):
    def post(self):
        # Get email and password from the request data
        data = request.get_json()
        email = data.get("email")
        password = data.get("password")

        # Check for missing email or password
        if not email or not password:
            return {"message": "Email and password are required!"}, 400

        # Check the email against the database
        user = User.query.filter_by(email=email).first()
        if not user:
            return {"message": "User not found!"}, 404

        # Verify the password using the check_password method
        if not user.check_password(password):
            return {"message": "Invalid password!"}, 401

        # If everything is okay, generate a new access token for the user
        access_token = create_access_token(identity=user.id)

        # Return the access token
        return {"access_token": access_token}, 200

# Add the new login route to the API
api.add_resource(UserLogin, "/login")

class AddToCart(Resource):
    def post(self):
        data = request.get_json()

        user_id = data.get('user_id')
        product_id = data.get('product_id')
        quantity = data.get('quantity', 1)

        # Validate the provided IDs
        user = User.query.get(user_id)
        product = Product.query.get(product_id)

        if not user or not product:
            return {"message": "User or product not found!"}, 404

        # Check if the product is already in the user's cart
        cart_item = CartItem.query.filter_by(user_id=user.id, product_id=product.id).first()

        if cart_item:
            # Increment the quantity if already in the cart
            cart_item.quantity += quantity
        else:
            # Otherwise, create a new cart item for this user and product
            cart_item = CartItem(user_id=user.id, product_id=product.id, quantity=quantity)
            db.session.add(cart_item)

        db.session.commit()
        return {"message": "Product added to cart successfully!"}, 201

api.add_resource(AddToCart, "/add-to-cart")

if __name__ == "__main__":
    app.run(port=5000, debug=True)
