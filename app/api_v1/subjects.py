from flask import jsonify, request
from ..models import Subject
from . import api


@api.route('/subjects/', methods=['GET'])
def get_subjects():
    return jsonify(subjects=Subject.get_subjects())


@api.route('/subjects/<int:id>', methods=['GET'])
def get_subject(id):
    subject = Subject.get_subject(id)
    if subject is None:
        res = jsonify()
        res.status_code = 404
        return res
    return jsonify({"subject": subject.export_data()})


@api.route('/subjects/', methods=['POST'])
def new_subject():
    data = request.json
    res = Subject.new_subject(data)
    if res == {}:
        res = jsonify()
        res.status_code = 201
        return res
    res = jsonify()
    res.status_code = 500
    return res


@api.route('/subjects/<int:id>', methods=['PUT'])
def update_subject(id):
    data = request.json
    res = Subject.update_subject(id, data)
    if res is None:
        res = jsonify()
        res.status_code = 404
        return res
    res = jsonify()
    res.status_code = 200
    return res


@api.route('/semesters/<int:id_semester>/subjects/', methods=['GET'])
def get_subject_by_semester(id_semester):
    return jsonify(semesters=Subject.get_subject_by_semester(id_semester))
