import hashlib

from flask import Blueprint, request

from constants.app_constants import GC
from database import db
from models.rooms import Room

delete_blueprint = Blueprint('delete', __name__, template_folder="templates")

@delete_blueprint.route('/delete', methods=['DELETE'])
def delete():

  token = request.headers.get('token', None)

  if not token:
    return "Access Token Missing"

  if hashlib.sha256(token.encode()).hexdigest() == GC.SECRET_KEY:
    to_delete = request.form.get("to_delete", None)

    if to_delete:

      if to_delete == "rooms":
        deleted = Room.query.delete()
        db.session.commit()

      return "Deleted {} rows from {}".format(deleted, to_delete)
    else:
      return "No to_delete key specified"

  else:

    return "Invalid Access Token"









