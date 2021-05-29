try:
    from __main__ import socketio
except ImportError:
    from app import socketio, app


@socketio.on('send_message')
def handle_send_message_event(data):

  print("{} has sent the message to the room {} : {}".format(data['username'],
                                                             data['room'],
                                                             data['message']))

  socketio.emit('receive_message', data, room=data['room'])