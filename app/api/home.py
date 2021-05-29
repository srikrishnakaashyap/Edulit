from flask import Blueprint, request, redirect, url_for, render_template
from flask_login import login_required, current_user

from constants.app_constants import GC

home_blueprint = Blueprint('home', __name__, template_folder="templates")

@home_blueprint.route('/')
@login_required
def home():

  course_list = []

  if current_user.role == GC.USER_ROLE.STUDENT:
    return render_template("student-dashboard.html", first_name=current_user.first_name,
                           course_list=course_list)
  elif current_user.role == GC.USER_ROLE.TEACHER:
    return render_template("teacher-dashboard.html", first_name=current_user.first_name,
                           course_list=course_list)
  elif current_user.role == GC.USER_ROLE.SYSTEM_ADMIN:
    return render_template("admin-dashboard.html", )
  else:
    return "Wrong Role"




