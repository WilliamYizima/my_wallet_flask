from flask import Flask

from wallet.ext import config
from wallet.ext import db

def create_app():
    app = Flask(__name__)

    config.init_app(app)
    db.init_app(app)
    return app