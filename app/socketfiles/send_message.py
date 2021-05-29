try:
    from __main__ import sockets
except ImportError:
    from app import sockets, app

@sockets.on('send_message')
def handle_send_message_event(data):

  print("{} has sent the message to the room {} : {}".format(data['username'],
                                                             data['room_id'],
                                                             data['message']))

  sockets.emit('receive_message', data, room=data['room_id'])

  print("SENT")


