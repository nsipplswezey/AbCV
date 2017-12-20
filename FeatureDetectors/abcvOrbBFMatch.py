import numpy as np
import cv2
import matplotlib.pyplot as plt
import sys

base = "./AbalonePhotos/"
query = base + sys.argv[1]
train = base + sys.argv[2]

img1 = cv2.imread(query,0)
img2 = cv2.imread(train,0)

#Initialize
orb = cv2.ORB_create()

# find keypoints and descriptors
kp1, des1 = orb.detectAndCompute(img1,None)
kp2, des2 = orb.detectAndCompute(img2,None)

# create BMatcher
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

# match
matches = bf.match(des1, des2)

# sort
matches = sorted(matches, key = lambda x:x.distance)

# draw first 10 matches
img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10],None,flags=2)

plt.imshow(img3),plt.show()
