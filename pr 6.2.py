import cv2
import numpy as np
import matplotlib.pyplot as plt

# -------------------------------
# Step 1: Read the damaged image
# -------------------------------
damaged_img = cv2.imread("cat_damaged.png")

# -------------------------------
# Step 2: Create mask automatically
# -------------------------------
height, width = damaged_img.shape[0], damaged_img.shape[1]

mask_auto = np.zeros((height, width, 3), dtype=np.uint8)

for i in range(height):
    for j in range(width):
        if damaged_img[i, j].sum() > 0:   # non-black pixel
            mask_auto[i, j] = [0, 0, 0]
        else:                              # damaged black pixel
            mask_auto[i, j] = [255, 255, 255]

# Convert mask to grayscale
mask_auto_gray = cv2.cvtColor(mask_auto, cv2.COLOR_BGR2GRAY)

# -------------------------------
# Step 3: Restore with TELEA method
# -------------------------------
restored_telea = cv2.inpaint(
    damaged_img,
    mask_auto_gray,
    3,
    cv2.INPAINT_TELEA
)

# -------------------------------
# Step 4: Restore with NS method
# -------------------------------
mask_predefined = cv2.imread("cat_mask.png", 0)

restored_ns = cv2.inpaint(
    damaged_img,
    mask_predefined,
    3,
    cv2.INPAINT_NS
)

# -------------------------------
# Step 5: Plot results
# -------------------------------
images = [
    damaged_img,
    mask_auto_gray,
    restored_telea,
    restored_ns
]

titles = [
    "Original Damaged",
    "Generated Mask",
    "Restored (Telea)",
    "Restored (Navier-Stokes)"
]

plt.figure(figsize=(12, 6))

for i in range(4):
    plt.subplot(2, 2, i + 1)

    if len(images[i].shape) == 2:
        # Grayscale mask
        plt.imshow(images[i], cmap="gray")
    else:
        # Convert BGR to RGB
        plt.imshow(cv2.cvtColor(images[i], cv2.COLOR_BGR2RGB))

    plt.title(titles[i])
    plt.axis("off")

plt.tight_layout()
plt.show()