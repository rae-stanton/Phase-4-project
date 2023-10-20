import os
import sys
from app import app
from models import User, Product, db
from faker import Faker
import random

# Get the current working directory
current_dir = os.path.dirname(os.path.abspath(__file__))

# Add the parent directory to sys.path
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

fake = Faker()

with app.app_context():
    from models import User, Product


# Function to seed users
def seed_users(num_users=10):
    User.query.delete()
    for _ in range(num_users):
        user = User(
            name=fake.first_name() + fake.last_name(),
            email=fake.unique.email(),
            password_hash=fake.password(),
            is_seller=fake.boolean(chance_of_getting_true=50)
        )
        db.session.add(user)
    db.session.commit()


# Function to seed products
def seed_products(num_products=9):
    Product.query.delete()
    for _ in range(num_products):
        num_categories = random.randint(1, 3)

        categories = [fake.random_element(elements=[
            'Aviator', 'Wayfarer', 'Round', 'Sports', 'Designer', 'Oversized', 'Cat-Eye'
        ]) for _ in range(num_categories)]

        if num_categories == 1:
            categories = [categories]

        product = Product(
            name=fake.city(),
            description=fake.sentence(),
            price=fake.random_int(min=10, max=200),
            image=fake.image_url(),
            count=fake.random_int(min=1, max=100),
            category=categories
        )
        db.session.add(product)
    db.session.commit()


# Function to seed other data (e.g., carts, orders, purchased, received) as needed
if __name__ == '__main__':
    with app.app_context():
        seed_users()
        seed_products()
        # Call other seed functions as needed


def seed_database():
    with app.app_context():
        existing_user = User.query.filter_by(
            email="example@example.com").first()

        if not existing_user:
            new_user = User(name="Example User",
                            email="example@example.com", is_seller=False)
            db.session.add(new_user)
            db.session.commit()
            print("Added new user!")
        else:
            print("User with given email already exists!")


if __name__ == "__main__":
    seed_database()
