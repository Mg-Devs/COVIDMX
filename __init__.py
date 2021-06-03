from flask import Flask, render_template
from flask import request
from dotenv import dotenv_values
import pymongo
from pymongo import MongoClient

config = dotenv_values(".env")
client = MongoClient(config.get("DB_URL"))
db = client.covidmx


def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = config.get("SECRET_KEY")

    # blueprint for auth routes in our app
    from auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    # blueprint for non-auth parts of app
    from main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(port=8080, debug=True)


