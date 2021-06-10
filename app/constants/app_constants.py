class GC:

  SECRET_KEY = "1f3424f5015c0eab6af85f76b41ac900ca6b23a8b48f059c1e34e3f1cb35d4c1"
  MAIL_USER_NAME = 'edulitapp@gmail.com'
  MAIL_PASSWORD = 'Edulitapp@123'

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

  class SIGNUP_EMAIL_TEMPLATES:

    WELCOME_SUBJECT = "Welcome to Edulit"

    WELCOME_BODY = """Dear {}
    
    Thank you for registering for Edulit. Please click the following link to verify your credentials. 
    
    Link: {}"""
