from flask import Blueprint, jsonify

from wallet.ext.api.services.request import request_mercadoBtc

bp = Blueprint("api", __name__)

@bp.route('/<coin>')
def index(coin):
    
    return jsonify(request_mercadoBtc(coin))