from flask import Blueprint, request, redirect, url_for, render_template
from flask_mail import Message
from sqlalchemy import exc
from werkzeug.security import generate_password_hash

from constants.app_constants import GC
from database import db
from models.users import User
from services.email_service import EmailService

signup_blueprint = Blueprint('signup', __name__, template_folder="templates")

@signup_blueprint.route('/signup', methods=['GET', 'POST'])
def signup():
  if request.method == 'POST':
    data = {
      "first_name": request.form.get("first_name", None),
      "last_name": request.form.get("last_name", None),
      "email": request.form.get("email", None),
      "password": generate_password_hash(request.form.get("password", None), method="sha256"),
      "role": int(request.form.get("role")) if request.form.get("role") is not None else None
    }

    user = User(data)

    try:
      EmailService.send_email(emails=user.email,
                              subject=GC.SIGNUP_EMAIL_TEMPLATES.WELCOME_SUBJECT,
                              body=GC.SIGNUP_EMAIL_TEMPLATES.WELCOME_BODY.format(user.first_name, "LINK"))
      db.session.add(user)
      db.session.commit()
      return redirect(url_for("login.login"))
    except exc.SQLAlchemyError as e:
      db.session.rollback()
      return render_template("signup.html")
  elif request.method == 'GET':
    return render_template("signup.html")