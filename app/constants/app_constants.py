class GC:

  SECRET_KEY = "kaashyap"

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