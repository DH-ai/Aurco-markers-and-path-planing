import cv2
from cv2.aruco import DICT_6X6_100
from cv2 import aruco

frame = cv2.imread("lp1.jpg")



vid = cv2.VideoCapture("feed/DSC_1797.MOV")

while (True):

    ret,frame = vid.read()
    gray_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    arucoDict = cv2.aruco.getPredefinedDictionary(aruco.DICT_4X4_100)
    arucoParams = cv2.aruco.DetectorParameters()
    detectors = cv2.aruco.ArucoDetector(arucoDict,arucoParams)
    corners, ids, rejectedCandidates = detectors.detectMarkers(gray_image)
    frame_markers = aruco.drawDetectedMarkers(frame.copy(), corners, ids)
    

    cv2.imshow("lol",frame_markers)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break