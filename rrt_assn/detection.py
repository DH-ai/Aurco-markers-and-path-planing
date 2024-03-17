import cv2 
from cv2 import aruco
import numpy as np
class Node():
    def __init__(self):
        pass


frame = cv2.imread("src/rrt_assn/rrt_assn/arucoMarker.jpg")
gray_img = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
arucoDict = cv2.aruco.getPredefinedDictionary(aruco.DICT_4X4_100)
arucoParams = cv2.aruco.DetectorParameters()
detectors = cv2.aruco.ArucoDetector(arucoDict,arucoParams)
corners, ids, rejectedMarkers = detectors.detectMarkers(gray_img)
im = (100)
if len(corners)>0:
    ids = ids.flatten()
    for (corner,id) in zip(corners,ids):
        corner =corner.reshape((4,2))
        (tl,tr,br,bl)= corner
        
        topLeft=(int(tl[0]),int(tl[1]))
        topRight=(int(tr[0]),int(tr[1]))
        bottomRight=(int(br[0]),int(br[1]))
        bottomLeft=(int(bl[0]),int(bl[1]))
        cv2.line(frame,topLeft,topRight,(0,0,255),2)
        cv2.line(frame,topRight,bottomRight,(0,0,255),2)
        cv2.line(frame,bottomRight,bottomLeft,(0,0,255),2)
        cv2.line(frame,bottomLeft,topLeft,(0,0,255),2)

cv2.imshow("markers",frame)
cv2.imshow("numpyarray",im)
cv2.waitKey(0)
cv2.destroyAllWindows()
