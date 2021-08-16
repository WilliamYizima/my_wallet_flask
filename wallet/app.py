from flask import Flask

from wallet.ext import config
from wallet.ext import db
from wallet.ext import cli
from wallet.ext import api


def create_app():
    """application factory flask"""
    app = Flask(__name__)

    config.init_app(app)
    db.init_app(app)
    cli.init_app(app)
    api.init_app(app)
    
    return app