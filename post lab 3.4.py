
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('input.jpg', cv2.IMREAD_GRAYSCALE)

if img is None:
    raise ValueError("Image not found. Please check the path and filename.")

sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)

sobel_edges = cv2.magnitude(sobelx, sobely)
sobel_edges = np.uint8(sobel_edges)

plt.figure(figsize=(10, 4))
plt.subplot(1, 2, 1)
plt.imshow(img, cmap='gray')
plt.title('Original Image')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(sobel_edges, cmap='gray')
plt.title('Sobel Edges CS24070')
plt.axis('off')

plt.tight_layout()
plt.show()

cv2.imwrite('sobel_edges.jpg', sobel_edges)