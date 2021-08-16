from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def init_app(app):
    """application factory for db"""
    db.init_app(app)