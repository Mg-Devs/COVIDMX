from flask import Flask, render_template
from flask import request
from flask_login import LoginManager, current_user
import pymongo
import os
from pymongo import MongoClient
from bson.objectid import ObjectId

client = MongoClient("MongoURL")
db = client.covidmx

def create_app():
    app = Flask(__name__, static_url_path='')

    app.config['SECRET_KEY'] = 'MongoKey'

    # blueprint for auth routes in our app
    from auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    # blueprint for non-auth parts of app
    from main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    from models import User

    @login_manager.user_loader
    def load_user(user_id):
        # since the user_id is just the primary key of our user table, use it in the query for the user
        return User(db.userAuth.find_one({'_id': ObjectId(user_id)}))

    return app

app = create_app()


