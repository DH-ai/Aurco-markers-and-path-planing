import cv2
import rclpy
from rclpy.node import Node
from cv_bridge import CvBridge
from sensor_msgs.msg import Image



class Vfn(Node):
    def __init__(self):
        super.__init__("VideoFeed")