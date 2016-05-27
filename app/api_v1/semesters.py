from flask import jsonify, request
from ..models import Semester
from . import api


@api.route('/semesters/', methods=['GET'])
def get_universities():
    return jsonify(semesters=Semester.get_semesters())


@api.route('/semesters/<int:id>', methods=['GET'])
def get_semester(id):
    semester = Semester.get_semester(id)
    if semester is None:
        res = jsonify()
        res.status_code = 404
        return res
    return jsonify({"semester": semester.export_data()})


@api.route('/semesters/', methods=['POST'])
def new_semester():
    data = request.json
    res = Semester.new_semester(data)
    if res == {}:
        res = jsonify()
        res.status_code = 201
        return res
    res = jsonify()
    res.status_code = 500
    return res


@api.route('/semesters/<int:id>', methods=['PUT'])
def update_semester(id):
    data = request.json
    res = Semester.update_semester(id, data)
    if res is None:
        res = jsonify()
        res.status_code = 404
        return res
    res = jsonify()
    res.status_code = 200
    return res


@api.route('/universities/<int:id_university>/semesters/', methods=['GET'])
def get_semester_by_university(id_university):
    return jsonify(semesters=Semester.get_semester_by_university(id_university))
