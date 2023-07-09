import pytesseract
import cv2

#load image
img=cv2.imread("images/receipt.jpg")
#convert bgr img to rgb img
img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

#config to detect only numbers from the image
config='digits'
#tesseract api needs rgb image
#print(pytesseract.image_to_string(img))

#map each character to its corresponding 4 bounding bounds and get the values
results=pytesseract.image_to_boxes(img, config=config)

ih, iw, ic=img.shape
for box in results.splitlines():
    box=box.split(' ')
    print(box)
    #get the four bounds
    x, y, w, h=int(box[1]), int(box[2]), int(box[3]), int(box[4])
    #draw a bounding box around each character
    cv2.rectangle(img,(x,ih-y), (w,ih-h), (0,255,0), 2)
    #display the character on the image slightly above the box
    cv2.putText(img, box[0], (x, ih-h), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 1)


cv2.imshow("Input",img)
cv2.waitKey(0)
