#open an image and do basic text recogniton
import pytesseract
import cv2
img = cv2.imread('images/test.jpg')
img = cv2.resize(img, (720, 480))
print(pytesseract.image_to_string(img))
cv2.imshow('Result', img)
cv2.waitKey(0)
