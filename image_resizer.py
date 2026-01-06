import cv2

# Load the image
image = cv2.imread("image.png")

# Check if image is loaded
if image is None:
    print("Error: Image not found!")
    exit()

# Predefined sizes (width, height)
sizes = {
    "small": (200, 200),
    "medium": (400, 400),
    "large": (600, 600)
}

# Resize, display, and save images
for name, size in sizes.items():
    resized_image = cv2.resize(image, size)

    # Show image
    cv2.imshow(name, resized_image)

    # Save image
    cv2.imwrite(f"{name}_image.jpg", resized_image)

# Wait and close windows
cv2.waitKey(0)
cv2.destroyAllWindows()
