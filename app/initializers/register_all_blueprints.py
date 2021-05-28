from api.home import home_blueprint
from api.room import room_blueprint
from api.login import login_blueprint


class RegisterBlueprints:

  def __init__(self, app, db):

    app.register_blueprint(home_blueprint)
    app.register_blueprint(room_blueprint)
    app.register_blueprint(login_blueprint)