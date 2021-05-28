
import os 
from math import sqrt

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
    # thumb_tip_y = hand_landmarks.landmark[4].y

    index_finger_MCP_x = (hand_landmarks.landmark[2].x)*w
    # index_finger_MCP_y = hand_landmarks.landmark[5].y



    return thumb_tip_x > index_finger_MCP_x

