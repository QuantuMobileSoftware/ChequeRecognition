import cv2
from pytesseract import image_to_string
from PIL import Image

def searchImage(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.medianBlur(gray, 15)
    edged = cv2.Canny(gray, 10, 120)

    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (7, 15))
    closed = cv2.morphologyEx(edged, cv2.MORPH_CLOSE, kernel)
    (cnts, _) = cv2.findContours(closed.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for c in cnts:
        peri = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.02 * peri, True)

    if len(approx) >= 4:
        if approx[0, 0, 0] < approx[1, 0, 0]:
            x1 = approx[0, 0, 0]
            y1 = approx[0, 0, 1]
        else:
            x1 = approx[1, 0, 0]
            y1 = approx[0, 0, 1]

        if approx[2, 0, 0] > approx[3, 0, 0]:
            x2 = approx[2, 0, 0]
            y2 = approx[2, 0, 1]
        else:
            x2 = approx[3, 0, 0]
            y2 = approx[2, 0, 1]

    cropped = img[y1:y2, x1:x2]
    height, width = cropped.shape[:2]
    center = (width / 2, height / 2)


    if (width > height):
        m = cv2.getRotationMatrix2D(center, 270, 1)
        rotated = cv2.warpAffine(cropped, m, (width, height))
        gray = cv2.cvtColor(rotated, cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(gray, (3, 3), 5)
        thresh = cv2.adaptiveThreshold(blur, 255, 1, 1, 11, 2)
        img = cv2.bitwise_not(thresh)
        cv2.imwrite('1.tif', img)
    else:
        rotated = cropped
        gray = cv2.cvtColor(rotated, cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(gray, (3, 3), 5)
        thresh = cv2.adaptiveThreshold(blur, 255, 1, 1, 11, 2)
        img = cv2.bitwise_not(thresh)
        cv2.imwrite('1.tif', img)


def searchAmount():
    total = image_to_string(Image.open('1.tif'), lang='rus')
    return total
