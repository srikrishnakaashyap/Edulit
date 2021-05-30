from flask_socketio import join_room

try:
    from __main__ import socketio
except ImportError:
    from app import socketio, app


@socketio.on('join_room')
def handle_join_room_event(data):

  join_room(data['room_id'])
  socketio.emit('join_room_announcement', data)
  # app.logger.info("{} has joined the room {}".format(data["username"], data["room"]))
  print("{} has joined the room {}".format(data["username"], data["room_id"]))