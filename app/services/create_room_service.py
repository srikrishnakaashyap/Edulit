
import random, string
class CreateRoomService:



  @staticmethod
  def get_room_id():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=10))