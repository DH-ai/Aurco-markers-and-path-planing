#!/usr/bin/env python

import cv2 
from cv2 import aruco
import numpy as np
import math

class Node():
    def __init__(self,x,y):
        self.x =x
        self.y = y
        self.path_x = []
        self.path_y = []

def collision(x1,y1,x2,y2):
    color=[]
    x = list(np.arange(x1,x2,(x2-x1)/100))
    y = []
    for x_cord in x:
        y.append(((y2-y1)/(x2-x1))*(x_cord-x1) + y1)
    for i in range(len(x)):
        color.append(sampling_image[int(y[i]),int(x[i])]) 
    return True if 0 in color else False
    # if (np.isin()) :
    #     return True
 

def checkCollisons(x1,y1,x2,y2):
    _,theta = dist_and_angle(x1,y1.x2,y2)
    x = x2+ stepSize*np.cos(theta)
    y = y2+ stepSize*np.size(theta)
    
    # checking the direct connection between the Q_new and the final end
    if collision(x,y,end[1],end[0]):
        direcCon = False
    else:
        direcCon = True
    
    #checks the connection between the two nodes
    if collision(x,y,x2,y2):
        nodeCon = False
    else:
        nodeCon = True

    return(x,y,direcCon,nodeCon) # return the coordinates for new node and direcCon-> if that new node directly connectes to the goal end or not and nodeCon-> if the rqandom genrated node has free path or not
    
def nearest_node(x,y):
    temp_dist=[]
    for i in range(len(node_list)):
        dist,_ = dist_and_angle(x,y,node_list[i].x,node_list[i].y)
        temp_dist.append(dist)
    return temp_dist.index(min(temp_dist)) # return the index of the node closest to the new node



def rnd_pnt():
    new_y = math.random.randint(0,len(frame))
    new_x = math,random.randint(0,len(frame[0]))
    return (new_y,new_x)
def dist_and_angle(x1,y1,x2,y2):
    dist = math.sqrt( ((x1-x2)**2)+((y1-y2)**2) )
    angle = math.atan2(y2-y1,x2-x1)
    return (dist,angle)


frame = cv2.imread("/home/dhruv/Desktop/MRT/rrt/src/rrt_assn/rrt_assn/arucoMarker.jpg") #(1080,1920,3)
start = (0,0)
end= (len(frame)-1,len(frame[0])-1)
stepSize = 20

cv2.circle(frame,(start[1]+10,start[0]+10),10,(0,255,0),4)
cv2.circle(frame,(end[1]-10,end[0]-10),10,(0,0,255),4)

node_list = [0]
node_list[0]= Node(start[0],start[1])
node_list[0].path_x.append(start[0])
node_list[0].path_y.append(start[1])
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
# cv2.imshow("Sampling Image",sampling_image)


cv2.imshow("Orignal Image",frame)

cv2.waitKey(0)
cv2.destroyAllWindows()
