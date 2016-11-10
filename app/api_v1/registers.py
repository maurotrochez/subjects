from flask import jsonify, request
from ..models import Registers
from . import api


@api.route('/temperature', methods=['GET'])
def get_last_temperature():
    return jsonify(temperature=Registers.get_last_temperature())


@api.route('/registers', methods=['POST'])
def post_register():
    try:
        data = request.json
        Registers.save_register(data)
        res = jsonify({})
        res.status_code = 201
        return res
    except Exception as e:
        print e
        raise e
