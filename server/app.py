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
        product_list = [{'name': product.name, 'description': product.description, 'price': product.price,
                         'image': product.image, 'count': product.count, 'category': product.category} for product in products]
        return jsonify(product_list)

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


class Carts(Resource):
    def get(self, user_id):
        user = User.query.get(user_id)
        if not user:
            return {"message": "User not found"}, 404

        cart_items = Cart.query.filter_by(user_id=user_id).all()
        cart_data = [{"product": cart_item.product.to_dict(
        ), "quantity": cart_item.quantity} for cart_item in cart_items]

        return {"user_id": user_id, "cart": cart_data}

    def post(self, user_id):
        data = request.get_json()
        product_id = data.get("product_id")
        quantity = data.get("quantity", 1)

        user = User.query.get(user_id)
        product = Product.query.get(product_id)

        if not user:
            return {"message": "User not found"}, 404
        if not product:
            return {"message": "Product not found"}, 404

        cart_item = Cart.query.filter_by(
            user_id=user_id, product_id=product_id).first()

        if cart_item:
            # Update quantity if the item already exists in the cart
            cart_item.quantity = quantity
        else:
            # Create a new cart item
            cart_item = Cart(
                user_id=user_id, product_id=product_id, quantity=quantity)
            db.session.add(cart_item)

        db.session.commit()

        return {"message": "Cart updated successfully"}

    def delete(self, user_id, product_id):
        cart_item = Cart.query.filter_by(
            user_id=user_id, product_id=product_id).first()

        if not cart_item:
            return {"message": "Cart item not found"}, 404

        db.session.delete(cart_item)
        db.session.commit()

        return {"message": "Cart item deleted successfully"}


api.add_resource(Carts, "/users/<int:user_id>/cart")
api.add_resource(Users, "/users")
api.add_resource(Products, "/products")

if __name__ == "__main__":
    app.run(port=5000, debug=True)
