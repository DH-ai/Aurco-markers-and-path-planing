import cv2 
from cv2 import aruco



dct= aruco.getPredefinedDictionary(aruco.DICT_4X4_100)
img = aruco.generateImageMarker(dictionary=dct,id=0,sidePixels=200)
while True:

    cv2.imshow("aruco",img)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break