
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from flask_cors import CORS
from flask_migrate import Migrate
from initializers.register_all_blueprints import RegisterBlueprints

app = Flask(__name__)

with app.app_context():
  from initializers.setup_config import SetupConfig
  SetupConfig(app)

  db = SQLAlchemy(app)
  migration = Migrate(app, db, directory="migrations", compare_type=True)

  cors = CORS(app)
  RegisterBlueprints(app, db)
  app.run(host="0.0.0.0", port=5000)


