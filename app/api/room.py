from flask import Blueprint, request, redirect, url_for, render_template
from flask_login import login_required

room_blueprint = Blueprint('room', __name__, template_folder="templates")

@room_blueprint.route('/join')
@login_required
def join_room():
  username = request.args.get('username')
  room = request.args.get('room')

  print(username, room)

  if username and room:
    return render_template('room.html', username=username, room=room)
  else:
    return redirect(url_for('home.home'))

