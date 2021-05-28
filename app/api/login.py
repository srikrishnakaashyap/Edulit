from flask import Blueprint, request, redirect, url_for, render_template

login_blueprint = Blueprint('login', __name__, template_folder="templates")

@login_blueprint.route('/login', methods=['GET'])
def login():

  return render_template("login.html")