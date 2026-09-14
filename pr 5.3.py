import cv2
import numpy as np

# Read the input image
img = cv2.imread("nature.jpg")

# Check if the image was loaded successfully
if img is None:
    print("Error: Image not found or path is incorrect.")
    exit()

# Apply Median Blur
dst = cv2.medianBlur(img, 5)

# Display original and blurred images side by side
cv2.imshow("CS24125 Original vs Median Blur", np.hstack((img, dst)))

# Wait for a key press and close all windows
cv2.waitKey(0)
cv2.destroyAllWindows()