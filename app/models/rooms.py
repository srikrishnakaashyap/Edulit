from models.users import User

try:
    from __main__ import db
except ImportError:
    from app import db



class Room(db.Model):
  __tablename__="rooms"

  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  name = db.Column(db.String(100))
  attendees = db.Column(db.PickleType())
  notes = db.Column(db.JSON())
  is_live = db.Column(db.Boolean)
  teacher_id = db.Column(db.Integer, db.ForeignKey(User.id, ondelete="CASCADE"), nullable=False)
  teacher = db.relationship('User', backref=db.backref('rooms', lazy='dynamic'))

  def __init__(self, kwargs):
    self.name = kwargs.get('name')
    self.attendees = kwargs.get('description')
    self.teacher_id = kwargs.get('teacher_id')

  @classmethod
  def getAll(cls):
    return Course.query.all()






