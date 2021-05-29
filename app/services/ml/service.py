
# import the opencv library
import cv2
from services.ml.draw_vid import mediapipe_results
import mediapipe as mp


vid = cv2.VideoCapture(0)
circles = []
prior,color_num = "dont_change", 0
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
    while(True):
        
        # Capture the video frame
        # by frame
        ret, frame = vid.read()
        frame, circles, pen_size, pen_color, prior, color_num = mediapipe_results(frame,circles,prior,color_num,pen_color,pen_size,mpHands,hands,mp_draw)
        
        print("pen_color : ",pen_color)
        for position in range(len(circles)): 
            pen_color = circles[position][1]
            frame = cv2.circle(frame, circles[position][0], pen_size, pen_color, -2)

        cv2.imshow('output', frame)
        if cv2.waitKey(1) and 0xFF == ord('q'):
            break

    vid.release()
    cv2.destroyAllWindows()
