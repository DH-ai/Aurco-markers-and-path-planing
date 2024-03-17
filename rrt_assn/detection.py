#!/usr/bin/env python

import cv2 
from cv2 import aruco
import numpy as np
import math
class Node():
    def __init__(self,x,y):
        self.x =x
        self.y = y
        self.parent_x = []
        self.parent_y = []

def collision(x1,y1,x2,y2):
    color=[]
    x = list(np.arange(x1,x2,(x2-x1)/100))
    y = []
    for x_cord in x:
        y.append(((y2-y1)/(x2-x1))*(x_cord-x1) + y1)
    for i in range(len(x)):
        color.append(sampling_image[int(y[i]),int(x[i])])
        
    for dim in color:
        if 0 in dim:
            return True
    return False
    # if (np.isin()) :
    #     return True
    # else: return False

box = list((np.arange(1,2,1/9),np.arange(2,1.5,1/9))) + list((np.arange(2,3,1/9),np.arange(1.5,3.5,1/9)))+list((np.arange(3,0,1/9),np.arange(3.5,3,1/9))) + list((np.arange(0,1,1/9),np.arange(3,2,1/9)))


frame = cv2.imread("/home/dhruv/Desktop/MRT/rrt/src/rrt_assn/rrt_assn/arucoMarker.jpg") #(1080,1920,3)

sampling_image = np.full((len(frame),len(frame[0])),255.0,dtype=np.uint8)

gray_img = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)




arucoDict = cv2.aruco.getPredefinedDictionary(aruco.DICT_4X4_100)
arucoParams = cv2.aruco.DetectorParameters()
detectors = cv2.aruco.ArucoDetector(arucoDict,arucoParams)
corners, ids, rejectedMarkers = detectors.detectMarkers(gray_img)


if len(corners)>0:
    ids = ids.flatten()
    for (corner,id) in zip(corners,ids):
        corner =corner.reshape((4,2))
        (tl,tr,br,bl)= corner
        
        topLeft=(int(tl[0]),int(tl[1]))
        topRight=(int(tr[0]),int(tr[1]))
        bottomRight=(int(br[0]),int(br[1]))
        bottomLeft=(int(bl[0]),int(bl[1]))
        # for frame or orignal image
        cv2.line(frame,topLeft,topRight,(0,0,255),2)
        cv2.line(frame,topRight,bottomRight,(0,0,255),2)
        cv2.line(frame,bottomRight,bottomLeft,(0,0,255),2)
        cv2.line(frame,bottomLeft,topLeft,(0,0,255),2)

        # for sampled image 
        cv2.line(sampling_image,topLeft,topRight,0,2)
        cv2.line(sampling_image,topRight,bottomRight,0,2)
        cv2.line(sampling_image,bottomRight,bottomLeft,0,2)
        cv2.line(sampling_image,bottomLeft,topLeft,0,2)


print(collision(348,408,352,463))
cv2.imshow("Sampling Image",sampling_image)


# print(sampling_image[1425][503])
# print(gray_img)

# cv2.imshow("markers",frame)

cv2.waitKey(0)
cv2.destroyAllWindows()
