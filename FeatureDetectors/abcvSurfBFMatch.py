import numpy as np
import cv2
import matplotlib.pyplot as plt
import sys

base = "./AbalonePhotos/"
query = base + sys.argv[1]
train = base + sys.argv[2]
hessian = int(sys.argv[3])
lines = int(sys.argv[4])

img1 = cv2.imread(query,0)
img2 = cv2.imread(train,0)

#Initialize
surf = cv2.xfeatures2d.SURF_create(400)
surf.setHessianThreshold(hessian)

# find keypoints and descriptors
kp1, des1 = surf.detectAndCompute(img1,None)
kp2, des2 = surf.detectAndCompute(img2,None)

# create BMatcher NORM_L2 for surf
bf = cv2.BFMatcher(cv2.NORM_L2, crossCheck=True)

# match
matches = bf.match(des1, des2)

# sort
matches = sorted(matches, key = lambda x:x.distance)

# draw first 10 matches
img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:lines],None,flags=2)

plt.imshow(img3),plt.show()
