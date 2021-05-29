from flask import Flask, render_template, Response
import cv2
#Initialize the Flask app
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

def gen_frames():  
    import cv2
    from draw_vid import mediapipe_results
    import mediapipe as mp


    camera = cv2.VideoCapture(0)
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

        while True:
            success, frame = camera.read()  # read the camera frame
            if not success:
                break
            else:

                frame, circles, pen_size, pen_color, prior, color_num = mediapipe_results(frame,circles,prior,color_num,pen_color,pen_size,mpHands,hands,mp_draw)
                
                print("pen_color : ",pen_color)
                for position in range(len(circles)): 
                    pen_color = circles[position][1]
                    frame = cv2.circle(frame, circles[position][0], pen_size, pen_color, -2)

                ret, buffer = cv2.imencode('.jpg', frame)
                frame = buffer.tobytes()
                yield (b'--frame\r\n'
                    b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # concat frame one by one and show result

if __name__ == "__main__":
    app.run(debug=True)