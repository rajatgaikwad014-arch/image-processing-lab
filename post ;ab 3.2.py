import cv2
img = cv2.imread("input.jpg")
t_lower = 100
t_upper = 200
aperture_size = 5
edge = cv2.Canny(img, t_lower, t_upper, apertureSize=aperture_size)
cv2.imshow('original', img)
cv2.imshow('CS24070 edge', edge)
cv2.waitKey(0)
cv2.destroyAllWindows()
