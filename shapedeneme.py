import cv2
import numpy as np

font = cv2.FONT_HERSHEY_COMPLEX #görüntüdeki metni görüntülemek için kullanacağımız yazı tipini tanımlıyoruz

img = cv2.imread("reall.jpeg", cv2.IMREAD_GRAYSCALE) #şekilleri greyscale yaptık
_, threshold = cv2.threshold(img, 90, 255, cv2.THRESH_BINARY) #arka planı beyaz ve tüm görüntüleri siyah yaptık eşik değeri vererek
contours, _ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) #bu komutla siyah beyaz görüntüden tüm şekillerin sınırlanı belirledik

#döngüye sokarız çünkü her şeklin kontur koordinatlarını alırız
for cnt in contours:
    approx = cv2.approxPolyDP(cnt, 0.01*cv2.arcLength(cnt, True), True)
    cv2.drawContours(img, [approx], 0, (0), 5)
    
    x = approx.ravel()[0]
    y = approx.ravel()[1]
    
    if len(approx) == 3:
        cv2.putText(img, "Triangle", (x, y), font, 1, (0))
    elif len(approx) == 4:
        cv2.putText(img, "Rectangle", (x, y), font, 1, (0))
    elif len(approx) == 5:
        cv2.putText(img, "Pentagon", (x, y), font, 1, (0))
    
    else:
        cv2.putText(img, "Circle", (x, y), font, 1, (0))

cv2.imshow("shapes", img)
cv2.imshow("Threshold", threshold)

cv2.waitKey(0)
cv2.destroyAllWindows()