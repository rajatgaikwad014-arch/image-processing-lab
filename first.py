import cv2
img = cv2.imread("Lotus.jpg", cv2.IMREAD_COLOR)
cv2.imshow("Ayush", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
