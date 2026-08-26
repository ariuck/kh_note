import cv2

img = cv2.imread("./images/45.png")


cv2.imshow("zzz", img[400:900,90:550])
cv2.waitKey(0)
