from models.users import User

try:
    from __main__ import db
except ImportError:
    from app import db



class Room(db.Model):
  __tablename__="rooms"

  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  name = db.Column(db.String(100))
  room_id = db.Column(db.String(10))
  attendees = db.Column(db.PickleType())
  notes = db.Column(db.JSON())
  is_live = db.Column(db.Boolean)
  created_by = db.Column(db.Integer, db.ForeignKey(User.id, ondelete="CASCADE"), nullable=False)
  user = db.relationship('User', backref=db.backref('rooms', lazy='dynamic'))

  def __init__(self, kwargs):
    self.name = kwargs.get('name')
    self.is_live = kwargs.get('is_live')
    self.created_by = kwargs.get('created_by')
    self.room_id = kwargs.get('room_id')

  def __repr__(self):
    return "{}, {}, {}".format(self.id, self.room_id, self.name)

  @classmethod
  def getAll(cls):
    return Room.query.all()






