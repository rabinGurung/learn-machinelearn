import cv2
import numpy as np
from  matplotlib import pyplot as plt

cv2.namedWindow('image',cv2.WINDOW_NORMAL)
img = cv2.imread('pixie.jpeg',0)
cv2.imshow('image',img) 
# key = cv2.waitKey(0)
# if key == 27:
# 	cv2.destroyAllWindows()
# elif key == ord('s'):
# 	cv2.imwrite('Messi.png',img)
# 	cv2.destroyAllWindows()

plt.imshow(img,cmap = 'gray',interpolation='bicubic')
plt.xticks([]),plt.yticks([])
plt.show()