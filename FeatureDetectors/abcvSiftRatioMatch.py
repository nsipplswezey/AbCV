import numpy as np
import cv2
import matplotlib.pyplot as plt
import sys

base = "./AbalonePhotos/"
query = base + sys.argv[1]
train = base + sys.argv[2]

img1 = cv2.imread(query,0)
img2 = cv2.imread(train,0)

#Init
sift = cv2.xfeatures2d.SIFT_create()

#kps and descriptors
kp1, des1 = sift.detectAndCompute(img1,None)
kp2, des2 = sift.detectAndCompute(img2,None)

#bf matcher
bf = cv2.BFMatcher()
matches = bf.knnMatch(des1,des2, k=2)

#ratio test
good = []
for m,n in matches:
    if m.distance < 0.75*n.distance:
        good.append([m])

#draw matches
img3 = cv2.drawMatchesKnn(img1,kp1,img2,kp2,good,None,flags=2)
plt.imshow(img3),plt.show()
