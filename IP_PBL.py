import cv2
import numpy as np
import matplotlib.pyplot as plt

# --------------------------------
# 1. Read Image
# --------------------------------

image = cv2.imread("try4.jpg")

if image is None:
    raise FileNotFoundError("Image not found.")

image = cv2.resize(image, (512, 512))

# Convert BGR to RGB
rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

SPLIT_THRESHOLD = 25
MERGE_THRESHOLD = 25
MIN_SIZE = 16

regions = []


# --------------------------------
# 2. Quadtree Splitting
# --------------------------------

def split_region(img, x, y, w, h):

    region = img[y:y+h, x:x+w]

    mean = np.mean(region, axis=(0, 1))
    std = np.mean(np.std(region, axis=(0, 1)))

    if std <= SPLIT_THRESHOLD or w <= MIN_SIZE or h <= MIN_SIZE:

        regions.append({
            "x": x,
            "y": y,
            "w": w,
            "h": h,
            "mean": mean
        })

        return

    w2 = w // 2
    h2 = h // 2

    split_region(img, x, y, w2, h2)
    split_region(img, x+w2, y, w-w2, h2)
    split_region(img, x, y+h2, w2, h-h2)
    split_region(img, x+w2, y+h2, w-w2, h-h2)


split_region(rgb, 0, 0, 512, 512)


# --------------------------------
# 3. Check if Regions are Neighbors
# --------------------------------

def are_neighbors(a, b):

    ax1, ay1 = a["x"], a["y"]
    ax2, ay2 = a["x"] + a["w"], a["y"] + a["h"]

    bx1, by1 = b["x"], b["y"]
    bx2, by2 = b["x"] + b["w"], b["y"] + b["h"]

    horizontal = (
        (ax2 == bx1 or bx2 == ax1)
        and max(ay1, by1) < min(ay2, by2)
    )

    vertical = (
        (ay2 == by1 or by2 == ay1)
        and max(ax1, bx1) < min(ax2, bx2)
    )

    return horizontal or vertical


# --------------------------------
# 4. Region Merging
# --------------------------------

merged = True

while merged:

    merged = False
    new_regions = []
    used = set()

    for i in range(len(regions)):

        if i in used:
            continue

        current = regions[i]

        for j in range(i + 1, len(regions)):

            if j in used:
                continue

            other = regions[j]

            difference = np.linalg.norm(
                current["mean"] - other["mean"]
            )

            if are_neighbors(current, other) \
                    and difference <= MERGE_THRESHOLD:

                # Keep both regions as one group
                current["members"] = current.get(
                    "members", [current]
                ) + other.get("members", [other])

                current["mean"] = (
                    current["mean"] + other["mean"]
                ) / 2

                used.add(j)
                merged = True

        new_regions.append(current)

    regions = new_regions


# --------------------------------
# 5. Terrain Classification
# --------------------------------

def classify_terrain(mean):

    r, g, b = mean

    brightness = (r + g + b) / 3

    # Water
    if b > r * 1.15 and b > g * 1.05:
        return "Water"

    # Vegetation
    elif g > r * 1.08 and g > b * 1.05:
        return "Vegetation"

    # Bare land
    elif r > b * 1.20 and g > b * 1.10:
        return "Bare Land"

    # Urban / built-up
    else:
        return "Urban Area"


# --------------------------------
# 6. Create Classification Image
# --------------------------------

classified = np.zeros_like(rgb)

# RGB display colors
colors = {
    "Water": (0, 0, 255),
    "Vegetation": (0, 180, 0),
    "Bare Land": (220, 150, 40),
    "Urban Area": (150, 150, 150)
}

class_count = {
    "Water": 0,
    "Vegetation": 0,
    "Bare Land": 0,
    "Urban Area": 0
}


for region in regions:

    label = classify_terrain(region["mean"])

    color = colors[label]

    x = region["x"]
    y = region["y"]
    w = region["w"]
    h = region["h"]

    # Draw only the actual region
    classified[y:y+h, x:x+w] = color

    class_count[label] += 1


# --------------------------------
# 7. Display Results
# --------------------------------

plt.figure(figsize=(15, 5))

plt.subplot(1, 3, 1)
plt.imshow(rgb)
plt.title("Original Image")
plt.axis("off")

plt.subplot(1, 3, 2)

# Show quadtree regions
quadtree = rgb.copy()

for region in regions:

    x = region["x"]
    y = region["y"]
    w = region["w"]
    h = region["h"]

    cv2.rectangle(
        quadtree,
        (x, y),
        (x+w, y+h),
        (255, 255, 255),
        1
    )

plt.imshow(quadtree)
plt.title("Quadtree Segmentation")
plt.axis("off")

plt.subplot(1, 3, 3)
plt.imshow(classified)
plt.title("Terrain Classification")
plt.axis("off")

plt.tight_layout()
plt.show()


# --------------------------------
# 8. Print Results
# --------------------------------

print("\nTerrain Classification:")

for label, count in class_count.items():
    print(label, ":", count, "regions")

print("\nTotal final regions:", len(regions))