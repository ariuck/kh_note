import cv2

img = cv2.imread('images/24.jpg')
img = cv2.resize(img, (500, 500))

cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
