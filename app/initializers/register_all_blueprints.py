from api.home import home_blueprint
from api.logout import logout_blueprint
from api.room import room_blueprint
from api.login import login_blueprint
from api.signup import signup_blueprint
from api.verify_email import verify_blueprint


class RegisterBlueprints:

  def __init__(self, app, db):

    app.register_blueprint(home_blueprint)
    app.register_blueprint(room_blueprint)
    app.register_blueprint(login_blueprint)
    app.register_blueprint(signup_blueprint)
    app.register_blueprint(logout_blueprint)
    app.register_blueprint(verify_blueprint)