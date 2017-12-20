import numpy as np
import cv2
import sys
from matplotlib import pyplot as plt
path = "./AbalonePhotos/" + sys.argv[1]
print(path)
img = cv2.imread(path)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

corners = cv2.goodFeaturesToTrack(gray,25,0.01,10)
corners = np.int0(corners)

for i in corners:
	x,y = i.ravel()
	cv2.circle(img,(x,y),3,255,-1)

plt.imshow(img),plt.show()	
