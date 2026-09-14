
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('input.jpg', cv2.IMREAD_GRAYSCALE)

if img is None:
    raise ValueError("Image not found. Please check the path and filename.")

kernelx = np.array([
    [-1, 0, 1],
    [-1, 0, 1],
    [-1, 0, 1]
], dtype=np.float32)

kernely = np.array([
    [-1, -1, -1],
    [0, 0, 0],
    [1, 1, 1]
], dtype=np.float32)

prewittx = cv2.filter2D(img, cv2.CV_64F, kernelx)
prewitty = cv2.filter2D(img, cv2.CV_64F, kernely)

prewitt_edges = cv2.magnitude(prewittx, prewitty)
prewitt_edges = np.uint8(prewitt_edges)

plt.figure(figsize=(10, 4))
plt.subplot(1, 2, 1)
plt.imshow(img, cmap='gray')
plt.title('Original Image')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(prewitt_edges, cmap='gray')
plt.title('Prewitt Edges CS24070')
plt.axis('off')

plt.tight_layout()
plt.show()

cv2.imwrite('prewitt_edges.jpg', prewitt_edges)