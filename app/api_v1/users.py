from flask import jsonify, request
from ..models import User
from . import api
import os
from oauth2client import client, crypt


@api.route('/validate_token', methods=['POST'])
def validate_token():
    try:
        token = request.json
        token = token[u'token']
        idinfo = client.verify_id_token(token, os.environ.get("CLIENT_ID"))
        # If multiple clients access the backend server:
        if idinfo['aud'] not in [os.environ.get("ANDROID_CLIENT_ID"), os.environ.get("WEB_CLIENT_ID")]:
            raise crypt.AppIdentityError("Unrecognized client.")
        if idinfo['iss'] not in ['accounts.google.com', 'https://accounts.google.com']:
            raise crypt.AppIdentityError("Wrong issuer.")
            # if idinfo['hd'] != APPS_DOMAIN_NAME:
            #     raise crypt.AppIdentityError("Wrong hosted domain.")
    except crypt.AppIdentityError as e:
        res = jsonify({"error": e})
        res.status_code = 401
        return res

    email = idinfo['email']
    name = idinfo['name']
    user = User.get_user_by_emial(email)
    # userid = idinfo['sub']
    if user is None:
        res = User.new_user({"email": email, "name": name})
        if res is not None:
            res = jsonify(res.export_data())
            res.status_code = 201
            return res
        res = jsonify()
        res.status_code = 500
        return res
    else:
        res = jsonify(user.export_data())
        res.status_code = 200
        return res


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
    return jsonify(user.export_data())


@api.route('/users/', methods=['POST'])
def new_user():
    data = request.json
    res = User.new_user(data)
    if res is not None:
        res = jsonify()
        res.status_code = 201
        return res
    res = jsonify()
    res.status_code = 500
    return res


@api.route('/users/<int:id>', methods=['PUT'])
def update_user(id):
    data = request.json
    res = User.update_user(id, data)
    if res is None:
        res = jsonify()
        res.status_code = 404
        return res
    res = jsonify()
    res.status_code = 200
    return res

