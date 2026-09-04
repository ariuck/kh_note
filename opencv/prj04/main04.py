#그리기, 주석

import cv2
import numpy as np

img = cv2.imread("./images/rgb.png")

#선 : cv2.line(이미지, 시작, 끝, 색, 두께)
# cv2.line(img, (0,0), (100,100), (255,255,255), 5)

# 사각형 : cv2.rectangle(이미지, 좌측상단, 우측하단, 색상, 두께)
cv2.rectangle(img, (10,10), (100,100), (255,0,0), 2)

# 원 : cv2.circle(이미지, 중심점 , 반지름 , 색상 , 두께)
cv2.circle(img, (100,100), 50, (0,0,255), -1)

# 다각형 : cv2.polylines( 이미지 , 점들 , 닫힘여부 , 색상 , 두께 )
pts = np.array([
    [10,10],
    [200,50],
    [400,300],
    [800,600],
    [50,70],
])
pts.reshape(-1,1,2)
cv2.polylines(img , [pts] , isClosed=True , color=(0,0,0) , thickness=10 )
cv2.fillPoly(img , [pts] , color=(0,0,0))

#텍스트 : cv2.putText(이미지, 텍스트, 위치, 폰트, 크기, 색, 굵기)
cv2.putText(img, "안녕하세요", (200,500), cv2.FONT_HERSHEY_SIMPLEX, 5, (0,0,255), 1)

cv2.imshow("img", img)
cv2.waitKey(0)
cv2.destroyAllWindows()