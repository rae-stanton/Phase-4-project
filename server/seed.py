from app import app
from models import User, db

def seed_database():
    with app.app_context():
        existing_user = User.query.filter_by(email="example@example.com").first()

        if not existing_user:
            new_user = User(name="Example User", email="example@example.com", is_seller=False)
            db.session.add(new_user)
            db.session.commit()
            print("Added new user!")
        else:
            print("User with given email already exists!")

if __name__ == "__main__":
    seed_database()
