from flask import Blueprint, request, jsonify
from services.students_services import *

student_route: Blueprint = Blueprint('student_route', __name__)

@student_route.route('/students', methods=['POST'])
def add_student_route():
    body = request.get_json()
    
    response_data, status_code = add_student_service(body)
    return jsonify(response_data), status_code

@student_route.route('/students', methods=['GET'])
def get_students_route():
    
    response_data, status_code = get_students_service()
    return jsonify(response_data), status_code