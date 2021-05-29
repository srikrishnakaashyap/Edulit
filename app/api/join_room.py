from flask import Blueprint, request, redirect, url_for, render_template
from flask_login import login_required, current_user

from models.rooms import Room

room_blueprint = Blueprint('room', __name__, template_folder="templates")

@room_blueprint.route('/join')
@login_required
def join_room():
  room_id = request.args.get('room_id')
  username = current_user.first_name

  room = Room.query.get(room_id)

  created_by = room.user.first_name





  if room_id:
    return render_template('DUMMY.html', room_id=room_id, username=username, room_name=room.name, created_by=created_by)
  else:
    return redirect(url_for('home.home'))

