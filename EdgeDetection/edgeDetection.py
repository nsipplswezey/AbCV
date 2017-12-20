import cv2
import numpy as np
from matplotlib import pyplot as plt
import sys
base = "./AbalonePhotos/"
query = base + sys.argv[1]

img = cv2.imread(query,0)
edges = cv2.Canny(img,150,200,True)

plt.subplot(121),plt.imshow(img,cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(edges,cmap = 'gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])

plt.show()
