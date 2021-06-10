from flask_mail import Message

from mail import mail

from constants.app_constants import GC


class EmailService:

  @classmethod
  def send_email(cls, subject=None, body=None, emails=None):
    if emails is None:
      emails = []

    if type(emails) == str:
      emails = [emails]

    msg = Message(
      subject,
      sender=GC.MAIL_USER_NAME,
      recipients=emails
    )
    msg.body = body

    sent = mail.send(msg)
    print(sent)
    return





