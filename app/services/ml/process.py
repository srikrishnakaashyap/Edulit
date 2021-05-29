import cv2
import mediapipe as mp

from services.ml.draw_vid import mediapipe_results


class Process:

  @classmethod
  def gen_frames(cls):
    camera = cv2.VideoCapture(0)
    circles = []
    prior, color_num = "dont_change", 0
    pen_color = 0
    pen_size = 15
    min_conf = 0.5
    max_hands = 2

    mpHands = mp.solutions.hands
    hands = mpHands.Hands(
      static_image_mode=False,
      max_num_hands=max_hands,
      min_detection_confidence=min_conf,
      min_tracking_confidence=min_conf
    )
    mp_draw = mp.solutions.drawing_utils

    with mpHands.Hands(
      min_detection_confidence=0.5,
      min_tracking_confidence=0.5) as hands:

      while True:
        success, frame = camera.read()  # read the camera frame
        if not success:
          break
        else:

          frame, circles, pen_size, pen_color, prior, color_num = mediapipe_results(frame, circles, prior, color_num,
                                                                                    pen_color, pen_size, mpHands, hands,
                                                                                    mp_draw)

          for position in range(len(circles)):
            pen_color = circles[position][1]
            frame = cv2.circle(frame, circles[position][0], pen_size, pen_color, -2)

          ret, buffer = cv2.imencode('.jpg', frame)
          frame = buffer.tobytes()
#           SocketService.broadcast(frame, room_id)

          yield (b'--frame\r\n'
                 b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')