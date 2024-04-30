import cv2
import os

# Create the 'outputs' folder if it doesn't exist
if not os.path.exists('outputs'):
    os.makedirs('outputs')

# Read the image
image = cv2.imread('image.jpg')

# Convert BGR to RGB
rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
cv2.imwrite('outputs/rgb.jpg', rgb)

# Convert BGR to Grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imwrite('outputs/grayscale.jpg', gray)

# Convert BGR to HSV
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
cv2.imwrite('outputs/hsv.jpg', hsv)

# Convert BGR to LAB
lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
cv2.imwrite('outputs/lab.jpg', lab)

# Convert BGR to YCrCb
ycrcb = cv2.cvtColor(image, cv2.COLOR_BGR2YCrCb)
cv2.imwrite('outputs/ycrcb.jpg', ycrcb)

# Convert BGR to HLS
hls = cv2.cvtColor(image, cv2.COLOR_BGR2HLS)
cv2.imwrite('outputs/hls.jpg', hls)

# Convert BGR to LUV
luv = cv2.cvtColor(image, cv2.COLOR_BGR2LUV)
cv2.imwrite('outputs/luv.jpg', luv)

# Convert RGB to BGR
bgr = cv2.cvtColor(rgb, cv2.COLOR_RGB2BGR)
cv2.imwrite('outputs/bgr.jpg', bgr)

print("Color space conversions completed. Output images saved in the 'outputs' folder.")