from flask import Blueprint, request, redirect, url_for, render_template, Response
from flask_login import login_required, current_user

from constants.app_constants import GC

from services.ml.process import Process

video_feed_blueprint = Blueprint('video_feed', __name__, template_folder="templates")

@video_feed_blueprint.route('/video_feed_home')
def video_feed_home():

  print("INSIDE VIDEO FEED")


  return render_template("index.html")


@video_feed_blueprint.route('/video_feed')
def video_feed():
  return Response(Process.gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')







