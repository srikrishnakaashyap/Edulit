from api.home import home_blueprint
from api.room import room_blueprint


class RegisterBlueprints:

  def __init__(self, app, db):

    app.register_blueprint(home_blueprint)
    app.register_blueprint(room_blueprint)