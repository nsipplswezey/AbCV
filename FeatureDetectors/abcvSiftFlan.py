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

#flann matcher
FLANN_INDEX_KDTREE = 1
index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)
search_params = dict(checks=50)

flann = cv2.FlannBasedMatcher(index_params,search_params)
matches = flann.knnMatch(des1,des2,k=2)

# Draw only good matches
matchesMask = [[0,0] for i in range(len(matches))]

# ratio test
for i,(m,n) in enumerate(matches):
	if m.distance < 0.7*n.distance:
		matchesMask[i]=[1,0]
		
draw_params = dict(matchColor = (0,255,0), singlePointColor = (255,0,0), matchesMask = matchesMask, flags = 0)

#draw matches
img3 = cv2.drawMatchesKnn(img1,kp1,img2,kp2,matches,None,**draw_params)                                                                                                                            
plt.imshow(img3),plt.show()
