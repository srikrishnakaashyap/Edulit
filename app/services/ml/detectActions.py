
import os 
from math import sqrt


def detectAction(hand_landmarks,image_shape):

    if erase(hand_landmarks,image_shape):
        return "Erase"
    
    if isDrawing(hand_landmarks,image_shape):
        return "Draw"
    
    return "dont_know"


def calc_distance(p1, p2): # simple function, I hope you are more comfortable
    return sqrt((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)

def erase(hand_landmarks,image_shape):

    h,w = image_shape
    index_finger_leftmost_x = (hand_landmarks.landmark[8].x)*w
    index_finger_leftmost_y = (hand_landmarks.landmark[8].y)*h

    middle_finger_tip_x = (hand_landmarks.landmark[12].x)*w
    middle_finger_tip_y = (hand_landmarks.landmark[12].y)*h

    index_finger_MCP_x = (hand_landmarks.landmark[5].x)*w
    index_finger_MCP_y = (hand_landmarks.landmark[5].y)*h

    pointA = (index_finger_leftmost_x, index_finger_leftmost_y) 
    pointB = (middle_finger_tip_x, middle_finger_tip_y) 
    pointC = (index_finger_MCP_x, index_finger_MCP_y) 
    
    distance1 = calc_distance(pointA, pointB) 
    distance2 = calc_distance(pointA, pointC) 
    return distance1 < distance2//3

def isDrawing(hand_landmarks,image_shape):

    _,w = image_shape

    thumb_tip_x = (hand_landmarks.landmark[4].x)*w
    index_finger_MCP_x = (hand_landmarks.landmark[2].x)*w

    return thumb_tip_x > index_finger_MCP_x

def landmark_extract(hand_lms, mpHands):

    output_lms = []

    lm_list = [
    mpHands.HandLandmark.WRIST, 
    mpHands.HandLandmark.THUMB_CMC, 
    mpHands.HandLandmark.THUMB_MCP,
    mpHands.HandLandmark.THUMB_IP, 
    mpHands.HandLandmark.THUMB_TIP, 
    mpHands.HandLandmark.INDEX_FINGER_MCP,
    mpHands.HandLandmark.INDEX_FINGER_DIP, 
    mpHands.HandLandmark.INDEX_FINGER_PIP, 
    mpHands.HandLandmark.INDEX_FINGER_TIP,
    mpHands.HandLandmark.MIDDLE_FINGER_MCP,
    mpHands.HandLandmark.MIDDLE_FINGER_DIP, 
    mpHands.HandLandmark.MIDDLE_FINGER_PIP, 
    mpHands.HandLandmark.MIDDLE_FINGER_TIP, 
    mpHands.HandLandmark.RING_FINGER_MCP, 
    mpHands.HandLandmark.RING_FINGER_DIP,
    mpHands.HandLandmark.RING_FINGER_PIP, 
    mpHands.HandLandmark.RING_FINGER_TIP, 
    mpHands.HandLandmark.PINKY_MCP,
    mpHands.HandLandmark.PINKY_DIP, 
    mpHands.HandLandmark.PINKY_PIP, 
    mpHands.HandLandmark.PINKY_TIP
    ]

    for lm in lm_list : 
        lms = hand_lms.landmark[lm]
        output_lms.append(lms.x)
        output_lms.append(lms.y)
        output_lms.append(lms.z)

    return output_lms

def checkColor(hand_landmarks,image_shape,prior,color_num):

    h,w = image_shape 
    curr_result = "dont_change"

    index_finger_leftmost_y = (hand_landmarks.landmark[8].y)*h
    index_finger_MCP_y = (hand_landmarks.landmark[5].y)*h
    wrist_y = (hand_landmarks.landmark[0].y)*h

    if wrist_y > index_finger_leftmost_y > index_finger_MCP_y:
        curr_result = "change"

    if prior == curr_result:
        return color_num,"dont_change" 

    print("CHANGED")
    return color_num+1,"change"
