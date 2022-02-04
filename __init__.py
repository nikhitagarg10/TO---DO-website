from flask import Flask

from .extentions import mongo
from  .main.routes import main

def create_app():
    app = Flask(__name__)

    app.config["MONGO_URI"] = "mongodb+srv://admin:I6iIABtt4YJJMYf8@flask.sopw8.mongodb.net/todoflask?retryWrites=true&w=majority"
    #name of the database is todoflask

    app.register_blueprint(main)

    mongo.init_app(app)

    return app