from constants.app_constants import GC


class SetupConfig:

  def __init__(self, app):

    app.config['DEBUG'] = True
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://avnadmin:jrqgc4boo8eruti9@hackon-mouryavsvp-6020.aivencloud.com:21508/defaultdb?sslmode=require"
    app.config['MAIL_SERVER'] = 'smtp.gmail.com'
    app.config['MAIL_PORT'] = 465
    app.config['MAIL_USERNAME'] = GC.MAIL_USER_NAME
    app.config['MAIL_PASSWORD'] = GC.MAIL_PASSWORD
    app.config['MAIL_USE_TLS'] = False
    app.config['MAIL_USE_SSL'] = True
    app.config['SECRET_KEY'] = GC.SECRET_KEY
