# Median Filter (for Salt & Pepper Noise)
import cv2
import matplotlib.pyplot as plt
# Read noisy image
img = cv2.imread("Ndog.jpg", 0)
# Apply Median Filter
restored = cv2.medianBlur(img, 5)
# Show results
plt.subplot(1, 2, 1), plt.imshow(img, cmap='gray'), plt.title("CS24073 Salt & Pepper Noise")
plt.subplot(1, 2, 2), plt.imshow(restored, cmap='gray'), plt.title("Restored (Median Filter)")
plt.show()

