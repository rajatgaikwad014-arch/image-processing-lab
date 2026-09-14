import numpy as np
import cv2 as cv
img = cv.imread('Sunflower.jpg', 0)
rows, cols = img.shape
M = np.float32([[1, 0, 180], [0, 1, 80]])
dst = cv.warpAffine(img, M, (cols, rows))
cv.imshow('Ayush', dst)
cv.waitKey(0)
cv.destroyAllWindows()
