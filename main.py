import cv2
import functions as f

img = cv2.imread('1')

height, width = img.shape[:2]
img = cv2.resize(img, (width / 3, height / 3), interpolation = cv2.INTER_CUBIC)

img = f.searchImage(img)
total = f.searchAmount()

print total