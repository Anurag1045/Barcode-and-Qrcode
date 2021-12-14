import cv2 as cv
from pyzbar import pyzbar

image = cv.imread("filename.ext")

#decode image
barcodes = pyzbar.decode(image)

for barcode in barcodes:
    x,y,w,h = barcode.rect

    #draw rectange over the code
    cv.rectangle(image, (x,y), (x+w, y+h), (255,0,0), 4)

    #convert into string
    bdata = barcode.data.decode("utf-8")
    btype = barcode.type
    text = f"{bdata}, {btype}"
    print("----")
    print(text)
    print("----")
    #write text on the image
    cv.putText(image, text,(x,y-10), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255),0)

cv.imshow("image", image)
cv.waitKey(0)