from api.courses import courses_blueprint
from api.create_room import create_room_blueprint
from api.delete import delete_blueprint
from api.get_all import get_all_blueprint
from api.home import home_blueprint
from api.logout import logout_blueprint
from api.join_room import room_blueprint
from api.login import login_blueprint
from api.signup import signup_blueprint
from api.verify_email import verify_blueprint
from api.video_feed import video_feed_blueprint


class RegisterBlueprints:

  def __init__(self, app, db):

    app.register_blueprint(home_blueprint)
    app.register_blueprint(room_blueprint)
    app.register_blueprint(login_blueprint)
    app.register_blueprint(signup_blueprint)
    app.register_blueprint(logout_blueprint)
    app.register_blueprint(verify_blueprint)
    app.register_blueprint(create_room_blueprint)
    app.register_blueprint(video_feed_blueprint)
    app.register_blueprint(courses_blueprint)
    app.register_blueprint(delete_blueprint)
    app.register_blueprint(get_all_blueprint)