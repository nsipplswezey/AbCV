import numpy as np
import cv2
import sys
from matplotlib import pyplot as plt
path = "./AbalonePhotos/" + sys.argv[1]
print(path)
img = cv2.imread(path)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)


sift = cv2.xfeatures2d.SIFT_create()
kp = sift.detect(gray,None)

img = cv2.drawKeypoints(gray,kp, None, color=(255,0,0), flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)


output = "sift_" + sys.argv[1]
cv2.imwrite(output,img)

