from datetime import datetime


class _:

  @staticmethod
  def get_current_time():

    return datetime.now().strftime("yyyy'-'MM'-'dd'T'HH':'mm':'ss")

