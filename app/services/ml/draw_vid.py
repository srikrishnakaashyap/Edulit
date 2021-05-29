import cv2
import time
import mediapipe as mp 
import numpy as np
from detectActions import *

## Video feed loop
# while True : 
#     success, frame = cap.read()


# def mediapipe_results(frame_infos):
def mediapipe_results(frame,circles,prior,color_num,pen_color,pen_size,mpHands,hands,mp_draw):
    #initialization---------------------------------------------------------------------------------------------------------->>>>>

    # frame = frame_infos["frame"]
    # circles = frame_infos["circles"]
    # prior = frame_infos["prior"]
    # color_num = frame_infos["color_num"]
    # pen_color = frame_infos["pen_color"]
    # pen_size = frame_infos["pen_size"]
    # mpHands = frame_infos["mpHands"],
    # hands = frame_infos["hands"],
    # mp_draw = frame_infos["mp_draw"]

    flip = True 
    
    eraser_size = 100
   
    ## cv2 text parameters
    font = cv2.FONT_HERSHEY_SIMPLEX
    fontScale = 1
    fontColor = (255,255,255)
    lineType = 4

    ## Stores previously drawing circles to give continous lines
    ptime = 0
    ctime = 0
    pen_color_changes = {0:"(255,0,0)",1:"(0,255,0)",2:"(0,0,255)",3:"(0,0,0)"}



    #code starts from here---------------------------------------------------------------------------------------------------------->>>>>

    if flip : 
        frame = cv2.flip(frame,1)
    h,w,c = frame.shape

    frame = cv2.resize(frame,(w*3,h*3))

    h = h*3
    w = w*3

    # frame = np.zeros([h,w,c],dtype=np.uint8)
    # frame.fill(255)

    img_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    print(hands)
    results = hands.process(img_rgb)
    # cv2.rectangle(frame, (w,h), (w-320,h-90), (0,0,0), -1, 1)

    if not results.multi_hand_landmarks : 
        # cv2.putText(frame, 'No hand in frame', (w-300, h-50), font, fontScale, fontColor, lineType)
        pass
    else : 
        for hand_landmarks in results.multi_hand_landmarks :
            mp_draw.draw_landmarks(frame, hand_landmarks, mpHands.HAND_CONNECTIONS)

            action = detectAction(hand_landmarks,(h,w))

            # cv2.putText(frame, f'Mode : {action}', (w-300, h-50), font, fontScale, fontColor, lineType)

            color_num, prior = checkColor(hand_landmarks,(h,w),prior,color_num)
            
            if prior=="change":
                pen_color = eval(pen_color_changes[color_num%4])
            
            ## Draw mode
            if action == 'Draw': 
                index_x = hand_landmarks.landmark[mpHands.HandLandmark.INDEX_FINGER_TIP].x
                index_y = hand_landmarks.landmark[mpHands.HandLandmark.INDEX_FINGER_TIP].y
                pos = [(int(index_x*w), int(index_y*h)),eval(pen_color_changes[color_num%4])]
               
                cv2.circle(frame, pos[0], 20, (0,0,0), 2)
                circles.append(pos)

            ## Erase mode
            elif action == 'Erase':
                eraser_mid = [
                        int(hand_landmarks.landmark[8].x * w),
                        int(hand_landmarks.landmark[8].y * h)
                    ]

                bottom_right = (eraser_mid[0]+eraser_size, eraser_mid[1]+eraser_size)
                top_left = (eraser_mid[0]-eraser_size, eraser_mid[1]-eraser_size)

                cv2.rectangle(frame, top_left, bottom_right, (0,0,255), 5)
                
                try : 
                    for pt in range(len(circles)):
                        if circles[pt][0][0]>top_left[0] and circles[pt][0][0]<bottom_right[0]: 
                            if circles[pt][0][1]>top_left[1] and circles[pt][0][1]<bottom_right[1]:
                                circles.pop(pt)
                except IndexError : 
                    pass
            
            elif action == "pause": 

                index_x = hand_landmarks.landmark[8].x
                index_y = hand_landmarks.landmark[8].y
                pos = (int(index_x*w), int(index_y*h))

                cv2.circle(frame, pos, 20, (0,0,255), 2)

    
    return frame, circles, pen_size, pen_color, prior, color_num

    ## Draws all stored circles 
    for position in range(len(circles)): 
        pen_color = circles[position][1]
        frame = cv2.circle(frame, circles[position][0], pen_size, pen_color, -2)
        frame = cv2.circle(frame, (circles[position][0][0],circles[position][0][1]+10), pen_size, pen_color, -2)
        frame = cv2.circle(frame, (circles[position][0][0],circles[position][0][1]-10), pen_size, pen_color, -2)

    ctime = time.time()
    fps = round(1/(ctime-ptime),2)
    ptime = ctime
    cv2.putText(frame, f'FPS : {str(fps)}', (w-300, h-20), font, fontScale, fontColor, lineType)

    return frame
