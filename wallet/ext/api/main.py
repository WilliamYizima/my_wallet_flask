from flask import Blueprint, jsonify, request

from wallet.ext.api.services.request import request_mercadoBtc

bp = Blueprint("api", __name__)

@bp.route('/', methods=['POST'])
def index():
    coin = request.args.get('coin')
    return jsonify(request_mercadoBtc(coin)), 201