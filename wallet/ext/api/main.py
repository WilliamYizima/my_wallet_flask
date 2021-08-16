from flask import Blueprint, jsonify

bp = Blueprint("api", __name__)

@bp.route('/')
def index():
    return jsonify({'teste':'teste'})