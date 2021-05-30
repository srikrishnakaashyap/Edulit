try:
    from __main__ import socketio
except ImportError:
    from app import socketio, app

class SocketService:

  @classmethod
  def broadcast(cls, frame, room_id):
    
    # print("FRAME", frame)
    socketio.emit('send_frame', frame, room=room_id)