try:
    from __main__ import db
except ImportError:
    from app import db

from flask_login import UserMixin
#
# @login_manager.user_loader
# def load_user(user_id):
#     return User.get(user_id)

class User(UserMixin, db.Model):
  __tablename__="users"

  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  first_name = db.Column(db.String(100))
  last_name = db.Column(db.String(100))
  email = db.Column(db.String(255), nullable=False, unique=True)
  password = db.Column(db.String(255), nullable=False)
  role = db.Column(db.Integer)
  # verified = db.Column(db.Boolean, default=False)

  def __init__(self, kwargs):
    self.first_name = kwargs.get('first_name')
    self.last_name = kwargs.get('last_name')
    self.email = kwargs.get('email')
    self.password = kwargs.get('password')
    self.role = kwargs.get('role')

  @classmethod
  def getAll(cls):
    return User.query.all()

  @classmethod
  def isVerified(cls, user_id):
    user = User.query.get(user_id)
    return user.verified
    # pass





