import cv2 as cv
img = cv.imread('Sunflower.jpg', 0)
cropped_img = img[100:300, 100:300]
cv.imshow('Ayush',cropped_img)
cv.imshow('img',img)
cv.imwrite('cropped_out.jpg', cropped_img)
cv.waitKey(0)
cv.destroyAllWindows()

