from models.users import User

try:
    from __main__ import db
except ImportError:
    from app import db



class Course(db.Model):
  __tablename__="courses"

  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  name = db.Column(db.String(100))
  description = db.Column(db.String(255))
  teacher_id = db.Column(db.Integer, db.ForeignKey(User.id, ondelete="CASCADE"), nullable=False)

  teacher = db.relationship('User', backref=db.backref('courses', lazy='dynamic'))

  # verified = db.Column(db.Boolean, default=False)

  def __init__(self, kwargs):
    self.name = kwargs.get('name')
    self.description = kwargs.get('description')
    self.teacher_id = kwargs.get('teacher_id')

  @classmethod
  def getAll(cls):
    return Course.query.all()






