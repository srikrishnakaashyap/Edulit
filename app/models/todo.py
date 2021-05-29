from models.users import User

try:
    from __main__ import db
except ImportError:
    from app import db



class Todo(db.Model):
  __tablename__="todos"

  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  content = db.Column(db.String(100))
  description = db.Column(db.String(255))
  created_by = db.Column(db.Integer, db.ForeignKey(User.id, ondelete="CASCADE"), nullable=False)
  user = db.relationship('User', backref=db.backref('courses', lazy='dynamic'))

  # verified = db.Column(db.Boolean, default=False)

  def __init__(self, kwargs):
    self.name = kwargs.get('name')
    self.description = kwargs.get('description')
    self.teacher_id = kwargs.get('teacher_id')

  @classmethod
  def getAll(cls):
    return Todo.query.all()






