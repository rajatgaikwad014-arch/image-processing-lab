import cv2

# Read image directly in grayscale mode
img = cv2.imread('input.jpg', cv2.IMREAD_GRAYSCALE)
# Check if the image was loaded properly if img is None:
# Check if the image was loaded properly if img is None:
# Check if the image was loaded properly
if img is None:
    print("Error: Image not found or unable to load.")
else:
# Show the grayscale
    cv2.imshow('CS24070 Grayscale Image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
