import numpy as np
import cv2 as cv
img = cv.imread('Sunflower.jpg', 0)
rows, cols = img.shape
img_shrinked = cv.resize(img, (300, 250),
                         interpolation=cv.INTER_AREA)
cv.imshow('img_shrnk', img_shrinked)
img_enlarged = cv.resize(img_shrinked, None,
                         fx=2, fy=1.5,
                         interpolation=cv.INTER_CUBIC)
cv.imshow('img_enlg', img_enlarged)
cv.waitKey(0)
cv.destroyAllWindows()

