from flask import Blueprint, redirect, url_for
from flask_login import login_required, logout_user

logout_blueprint = Blueprint('logout', __name__, template_folder="templates")

@logout_blueprint.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("login.login"))