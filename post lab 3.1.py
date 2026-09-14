import cv2
import matplotlib.pyplot as plt
import numpy as np

image_path = "input.jpg"

image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

if image is None:
    print("Error: Image not found")
    exit()

blurred_image = cv2.GaussianBlur(image, (5, 5), 1.4)

edges = cv2.Canny(blurred_image, 50, 150)

plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.title("Original Image")
plt.imshow(image, cmap="gray")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.title("Edge Detected Image || CS24070")
plt.imshow(edges, cmap="gray")
plt.axis("off")

plt.show()