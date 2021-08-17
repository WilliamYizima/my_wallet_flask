from flask import Blueprint, jsonify, request
import datetime

from wallet.ext.api.services.request import bulk_insert_db
from wallet.ext.db.models import Gains

bp = Blueprint("api", __name__)

@bp.route('/populate', methods=['POST'])
def create_data_in_db():
    """populate db with data last 3 days"""
    try:
        coin = request.args.get('coin')
        result_data = bulk_insert_db(cripto=coin)

        for data_gain in result_data['result']:
            formatted_date = datetime.datetime.strptime(
                                            data_gain.date, '%Y-%m-%d')

            gains = Gains.add_gains(
                        description=data_gain.description, 
                        amount=data_gain.amount,
                        date=formatted_date)

        return jsonify(bulk_insert_db(cripto=coin)), 201
    except Exception as e:
        return jsonify({'error':e}), 500

@bp.route('/', methods=['GET'])
def get_all():
    """return all"""
    try:
        gains = Gains.query.all()
        gain_attributes = [gain.to_json() for gain in gains]
        return jsonify({'result':gain_attributes}),200
    except:
        return jsonify({'error':"don't have data"}), 500

@bp.route('/<id>', methods=['GET'])
def get_one(id):
    """return one"""
    try:
        gains = Gains.query.filter_by(id=id).one()
        
        return jsonify({'result':gains.to_json()}), 200
    except:
        return jsonify({'error':"don't have id"}), 500

@bp.route('/<id>', methods=['DELETE'])
def delete(id):
    """delete a data"""
    try:
        gains = Gains.delete_gains(id)
        return jsonify(), 204
    except:
        return jsonify({'msg':'not deleted'}),500
