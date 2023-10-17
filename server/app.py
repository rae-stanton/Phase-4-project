from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from server.user_model import User

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///shoppingapp.db'

db = SQLAlchemy(app)
migrate = Migrate(app, db)

@app.route('/')
def index():
    return 'Hello, World!'


if __name__ == '__main__':
    app.run()
