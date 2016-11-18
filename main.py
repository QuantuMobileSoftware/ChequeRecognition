import cv2
import functions as f
import os

img = cv2.imread('img.jpg')

height, width = img.shape[:2]
img = cv2.resize(img, (width / 3, height / 3), interpolation = cv2.INTER_CUBIC)

img_path = f.searchImage(img)
total = f.searchAmount(img_path)

os.remove(img_path)

print total
