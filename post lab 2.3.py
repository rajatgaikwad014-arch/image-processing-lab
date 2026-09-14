import cv2
img = cv2.imread('input.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
cv2.imshow('CS24070 image', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
