import cv2
import numpy as np
bottom_left=cv2.imread("images/bottom_left.jpg")
bottom_right=cv2.imread("images/bottom_right.jpg")
top_left=cv2.imread("images/top_left.jpg")
top_right=cv2.imread("images/top_right.jpg")
final=cv2.imread("images/sample_image.jpg")

h_stack1=np.hstack([top_left,top_right])
h_stack2=np.hstack([bottom_left,bottom_right])

v_stack=np.vstack([h_stack1,h_stack2])
cv2.imshow("collage",v_stack)
cv2.waitKey(0)
