from flask import jsonify, request
from ..models import User
from . import api


@api.route('/users/', methods=['GET'])
def get_users():
    return jsonify(users=User.get_users())


@api.route('/users/<int:id>', methods=['GET'])
def get_user(id):
    user = User.get_user(id)
    if user is None:
        res = jsonify()
        res.status_code = 404
        return res
    return jsonify({"user": user.export_data()})


@api.route('/users/', methods=['POST'])
def new_user():
    data = request.json
    res = User.new_user(data)
    if res == {}:
        res = jsonify()
        res.status_code = 201
        return res
    res = jsonify()
    res.status_code = 500
    return res
