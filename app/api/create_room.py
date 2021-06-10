from flask import Blueprint, request, redirect, url_for, render_template
from flask_login import login_required, current_user
from sqlalchemy import exc

from constants.app_constants import GC
from database import db
from models.rooms import Room
from services._ import _
from services.create_room_service import CreateRoomService

create_room_blueprint = Blueprint('create_room', __name__, template_folder="templates")

@create_room_blueprint.route('/createroom', methods=['POST'])
@login_required
def create_room():
  room_name = request.form.get("room", None)

  if room_name == None:
    room_name = _.get_current_time()

  userId = current_user.id

  room_id = CreateRoomService.get_room_id()

  data = {
    "name": room_name,
    "created_by": userId,
    "is_live": True,
    "room_id": room_id
  }
  room = Room(data)

  try:
    db.session.add(room)
    db.session.commit()
    return redirect("/join?room_id={}".format(room_id))
  except exc.SQLAlchemyError as e:
    print(e)
    db.session.rollback()
    return redirect("home.home")















