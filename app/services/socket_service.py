try:
    from __main__ import sockets
except ImportError:
    from app import sockets, app

class SocketService:

  @classmethod
  def broadcast(cls, frame, room_id):
    
    # print("FRAME", frame)
    sockets.emit('send_frame', frame, room=room_id)