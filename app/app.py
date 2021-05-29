from flask_login import LoginManager
from flask_socketio import SocketIO
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from flask_cors import CORS
from flask_migrate import Migrate

from database import db
from initializers.register_all_blueprints import RegisterBlueprints

app = Flask(__name__)

with app.app_context():
  from initializers.setup_config import SetupConfig
  SetupConfig(app)

  login_manager = LoginManager()

  db.init_app(app)
  migration = Migrate(app, db, directory="migrations", compare_type=True)

  login_manager.init_app(app)
  login_manager.login_view = 'login.login'

  from models.users import User

  @login_manager.user_loader
  def load_user(user_id):
    # since the user_id is just the primary key of our user table, use it in the query for the user
    return User.query.get(int(user_id))

  cors = CORS(app)
  RegisterBlueprints(app, db)
  socketio = SocketIO(app, cors_allowed_origins='*')
  import sockets.join_room
  import sockets.send_message
  socketio.run(app, host="0.0.0.0", port=5000, debug=True)


