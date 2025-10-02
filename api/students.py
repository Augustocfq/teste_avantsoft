from flask import Blueprint, request
from services.students_services import *

student_route: Blueprint = Blueprint('student_route', __name__)