#!/usr/bin/env python
from __future__ import print_function

import sys
import rospy
import cv2
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import message_filters

class image_converter:

  def __init__(self):
    self.image_pub_left = rospy.Publisher("/stereo_publisher/left/converted/image/",Image, queue_size=10)
    self.image_pub_right = rospy.Publisher("/stereo_publisher/right/converted/image/",Image, queue_size=10)

    self.bridge = CvBridge()
    self.image_sub_left = message_filters.Subscriber("/stereo_publisher/left/image",Image)
    self.image_sub_right = message_filters.Subscriber("/stereo_publisher/right/image",Image)

    ts = message_filters.TimeSynchronizer([self.image_sub_left, self.image_sub_right], 10)
    ts.registerCallback(self.synchron_callback)

  def synchron_callback(self, data_left, data_right):

    left_img = self.bridge.imgmsg_to_cv2(data_left, '8UC1')
    right_img = self.bridge.imgmsg_to_cv2(data_right, '8UC1')

    self.image_pub_left.publish(self.bridge.cv2_to_imgmsg(left_img, 'mono8'))
    self.image_pub_right.publish(self.bridge.cv2_to_imgmsg(right_img, 'mono8'))

  # def callback_left(self,data):
  #   data.encoding = "mono8"
  #   try:
  #     cv_image = self.bridge.imgmsg_to_cv2(data, "mono8")
  #   except CvBridgeError as e:
  #     print(e)

  #   # (rows,cols,channels) = cv_image.shape
  #   # if cols > 60 and rows > 60 :
  #   #   cv2.circle(cv_image, (50,50), 10, 255)

  #   # cv2.imshow("Image window", cv_image)
  #   # cv2.waitKey(3)

  #   try:
  #     self.image_pub_left.publish(self.bridge.cv2_to_imgmsg(cv_image, "mono8"))
  #   except CvBridgeError as e:
  #     print(e)

  # def callback_right(self,data):
  #   data.encoding = "mono8"
  #   try:
  #     cv_image = self.bridge.imgmsg_to_cv2(data, "mono8")
  #   except CvBridgeError as e:
  #     print(e)

  #   # (rows,cols,channels) = cv_image.shape
  #   # if cols > 60 and rows > 60 :
  #   #   cv2.circle(cv_image, (50,50), 10, 255)

  #   # cv2.imshow("Image window", cv_image)
  #   # cv2.waitKey(3)

  #   try:
  #     self.image_pub_right.publish(self.bridge.cv2_to_imgmsg(cv_image, "mono8"))
  #   except CvBridgeError as e:
  #     print(e)


def main(args):
  rospy.init_node('image_converter', anonymous=True)
  ic = image_converter()

  try:
    rospy.spin()
  except KeyboardInterrupt:
    print("Shutting down")
  cv2.destroyAllWindows()

if __name__ == '__main__':
    main(sys.argv)
