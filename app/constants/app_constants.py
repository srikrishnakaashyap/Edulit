class GC:

  SECRET_KEY = "1f3424f5015c0eab6af85f76b41ac900ca6b23a8b48f059c1e34e3f1cb35d4c1"

  class USER_ROLE:
    SYSTEM_ADMIN = 0
    TEACHER = 6
    STUDENT = 10

    def get_all(cls):
      return cls.TEACHER, cls.STUDENT

    def get_name(self, role):

      if role == 6:
        return "TEACHER"
      elif role == 10:
        return "STUDENT"