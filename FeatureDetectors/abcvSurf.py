import numpy as np
import cv2
import sys
from matplotlib import pyplot as plt
path = "./AbalonePhotos/" + sys.argv[1]
print(len(sys.argv) < 3)
hessian = 500 if (len(sys.argv) < 3) else int(sys.argv[2]) 
print(path)
img = cv2.imread(path,0)


surf = cv2.xfeatures2d.SURF_create(400)
kp, des = surf.detectAndCompute(img,None)

print(len(kp))
surf.setHessianThreshold(hessian)
kp, des = surf.detectAndCompute(img,None)
print(len(kp))

img2 = cv2.drawKeypoints(img,kp, None,(255,0,0),4)
plt.imshow(img2),plt.show()

