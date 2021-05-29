from flask import Blueprint, request, redirect, url_for, render_template
from flask_login import login_required, current_user

from constants.app_constants import GC

courses_blueprint = Blueprint('courses', __name__, template_folder="templates")

@courses_blueprint.route('/courses')
@login_required
def home():

  course_list = []

  return render_template("teacher-course-dashboard.html", course_list=course_list)









