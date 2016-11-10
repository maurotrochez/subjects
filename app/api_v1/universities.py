from flask import jsonify, request, Response, json
from ..models import University
from . import api


@api.route('/universities', methods=['GET'])
def get_universities():
    return jsonify(universities=University.get_universities())


@api.route('/universities/<int:id>', methods=['GET'])
def get_university(id):
    university = University.get_university(id)
    if university is None:
        res = jsonify()
        res.status_code = 404
        return res
    return jsonify(university.export_data())


@api.route('/universities', methods=['POST'])
def new_university():
    data = request.json
    res = University.new_university(data)
    if res == {}:
        res = jsonify()
        res.status_code = 201
        return res
    res = jsonify()
    res.status_code = 500
    return res


@api.route('/universities/<int:id>', methods=['PUT'])
def update_university(id):
    data = request.json
    res = University.update_university(id, data)
    if res is None:
        res = jsonify()
        res.status_code = 404
        return res
    res = jsonify()
    res.status_code = 200
    return res


@api.route('/users/<int:id_user>/universities/', methods=['GET'])
def get_university_by_user(id_user):
    data = University.get_university_by_user(id_user)
    print data
    # res = json.dumps(univ.export_data() for univ in University.get_university_by_user(id_user))
    return Response(status=200, response=json.dumps(data))
    # return jsonify([univ.export_data() for univ in University.get_university_by_user(id_user)])
