import cv2

image = cv2.imread('input.jpg')

if image is None:
    print("Error: Image not found or failed to load.")
    exit()

lab_image = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)

cv2.imshow('LAB Image || CS24070', lab_image)

cv2.waitKey(0)
cv2.destroyAllWindows()