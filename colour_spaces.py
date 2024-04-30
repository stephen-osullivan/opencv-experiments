import cv2

# Read the image
image = cv2.imread('image.jpg')

# Display the original image
cv2.imshow('Original Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Convert to Grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow('Grayscale', gray)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Convert to HSV
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
cv2.imshow('HSV', hsv)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Convert to LAB
lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
cv2.imshow('LAB', lab)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Convert to YCrCb
ycrcb = cv2.cvtColor(image, cv2.COLOR_BGR2YCrCb)
cv2.imshow('YCrCb', ycrcb)
cv2.waitKey(0)
cv2.destroyAllWindows()