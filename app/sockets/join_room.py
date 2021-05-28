try:
    from __main__ import socketio
except ImportError:
    from app import socketio, app


@socketio.on('join_room')
def handle_join_room_event(data):
  # app.logger.info("{} has joined the room {}".format(data["username"], data["room"]))
  print("{} has joined the room {}".format(data["username"], data["room"]))