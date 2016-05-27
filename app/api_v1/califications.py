from flask import jsonify, request
from ..models import Calification
from . import api


@api.route('/califications/', methods=['GET'])
def get_califications():
    return jsonify(califications=Calification.get_califications())


@api.route('/califications/<int:id>', methods=['GET'])
def get_calification(id):
    calification = Calification.get_calification(id)
    if calification is None:
        res = jsonify()
        res.status_code = 404
        return res
    return jsonify({"calification": calification.export_data()})


@api.route('/califications/', methods=['POST'])
def new_subject():
    data = request.json
    res = Calification.new_calification(data)
    if res == {}:
        res = jsonify()
        res.status_code = 201
        return res
    res = jsonify()
    res.status_code = 500
    return res


@api.route('/califications/<int:id>', methods=['PUT'])
def update_calification(id):
    data = request.json
    res = Calification.update_calification(id, data)
    if res is None:
        res = jsonify()
        res.status_code = 404
        return res
    res = jsonify()
    res.status_code = 200
    return res


@api.route('/subjects/<int:id_subject>/califications/', methods=['GET'])
def get_calification_by_subject(id_subject):
    return jsonify(califications=Calification.get_calification_by_subject(id_subject))
