from app_socket import socketio

class SocketService:

  @classmethod
  def broadcast(cls, frame, room_id):
    pass

    socketio.emit('send_frame', frame, room=room_id)