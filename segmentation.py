#!/usr/bin/env python
import cv2
import numpy as np
import serial 

cap = cv2.VideoCapture(0)

ser = serial.Serial("/dev/ttyACM0", baudrate = 115200)
while True:
    _, frame = cap.read()
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # Red color
    #low_red = np.array([161, 155, 84])
    #high_red = np.array([179, 255, 255])
    #red_mask = cv2.inRange(hsv_frame, low_red, high_red)
    #red = cv2.bitwise_and(frame, frame, mask=red_mask)

        # Blue color
    low_blue = np.array([94, 80, 2])  
    high_blue = np.array([126, 255, 255]) #hsv color 
    blue_mask = cv2.inRange(hsv_frame, low_blue, high_blue)
    blue = cv2.bitwise_and(frame, frame, mask=blue_mask)

    # Green color
    low_green = np.array([110, 50, 50])
    high_green = np.array([200, 255, 255])
    green_mask = cv2.inRange(hsv_frame, low_green, high_green)
    green = cv2.bitwise_and(frame, frame, mask=green_mask)

    # Every color except white
    low = np.array([0, 42, 0])
    high = np.array([179, 255, 255])
    mask = cv2.inRange(hsv_frame, low, high)
    result = cv2.bitwise_and(frame, frame, mask=mask)


    contours, _ = cv2.findContours(green_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    for contour in contours:
    	cv2.drawContours(frame, contour, -1, (0, 255, 0), 3)



    nonzero = cv2.countNonZero(green_mask)

    if nonzero >= 12000 and nonzero <= 60000:
    	ser.write("h")
    	print("detcte")
    elif nonzero > 60000:
   		ser.write("s")
   		print("muy cerca")
    else:
    	ser.write("a") 
    	print("nada aun")

    cv2.imshow("Frame", frame)
    cv2.imshow("Red", green_mask)
    #cv2.imshow("Blue", blue)
    cv2.imshow("Green", green)
    cv2.imshow("Result", result)
    print(nonzero)
    key = cv2.waitKey(1)
    if key == 27:
        break



    nonzero = cv2.countNonZero(green_mask)

    if nonzero >= 12000 and nonzero <= 60000:
    	ser.write("h")
    	print("detcte")


   	if nonzero >= 60000:
   		ser.write("a")
   		print("muy cerca")
    else:
    	ser.write("a") 
    	print("nada aun")

    cv2.imshow("Frame", frame)
    cv2.imshow("Red", green_mask)
    #cv2.imshow("Blue", blue)
    cv2.imshow("Green", green)
    cv2.imshow("Result", result)
    print(nonzero)
    key = cv2.waitKey(1)
    if key == 27:
        break
