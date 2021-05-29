from flask import Blueprint, request, redirect, url_for, render_template, Response
from flask_login import login_required, current_user

from constants.app_constants import GC

from services.ml.process import Process

video_feed_blueprint = Blueprint('video_feed', __name__, template_folder="templates")

@video_feed_blueprint.route('/video_feed')
@login_required
def video_feed():

  room_id = request.args.get("room_id")

  return Response(Process.gen_frames(room_id), mimetype='multipart/x-mixed-replace; boundary=frame')







