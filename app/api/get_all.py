import hashlib

from flask import Blueprint, request

from constants.app_constants import GC
from models.rooms import Room
from models.users import User

get_all_blueprint = Blueprint('get_all', __name__, template_folder="templates")

@get_all_blueprint.route('/get_all', methods=['GET'])
def get_all():

  token = request.headers.get('token', None)

  if not token:
    return "Access Token Missing"

  if hashlib.sha256(token.encode()).hexdigest() == GC.SECRET_KEY:
    get = request.form.get("get", None)

    if get:

      if get == "rooms":
        data = Room.getAll()

        print(data)

      if get == "users":
        data = User.getAll()
        print(data)

      return "Fetched {} rows from {}".format(len(data), get)
    else:
      return "No to_delete key specified"

  else:

    return "Invalid Access Token"









