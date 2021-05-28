from flask import Blueprint, request, redirect, url_for, render_template

from services.verify_user import VerifyUser

verify_blueprint = Blueprint('verify', __name__, template_folder="templates")

@verify_blueprint.route('/verifyemail')
def join_room():
  key = request.args.get('auth_key')

  if VerifyUser.check_user_hash():
    pass
    #query database and update verified to True
  else:
    return

