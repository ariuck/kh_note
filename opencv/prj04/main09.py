#모폴로지(  침식 or 팽창)
#(이진화 처리 알아야할듯)
#(이진화 처리에서 생긴 노이즈 점들을 해결해주는듯)
import cv2
import numpy as np

#이미지 준비
img = np.zeros((300,300),np.uint8)

cv2.rectangle(img,(100,100),(200,200),(255,255,255),-1)
cv2.circle(img,(150,150),5,(0,0,0),-1)
cv2.circle(img,(40,40),3,(255,255,255),-1)

kn = np.ones((5,5),dtype=np.uint8)
# #침식
# result_e = cv2.erode(img,kn,iterations = 1)
# #팽창
# result_d = cv2.dilate(img,kn,iterations = 1)

#모폴로지(모폴리지 연산을 보면 open과 close가 있음 open은 침식 -> 팽창,close는 팽창 ->침식 세트로 해줌)
img_open = cv2.morphologyEx(img, cv2.MORPH_OPEN, kn)
img_close = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kn)
img_gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kn)

cv2.imshow("img", img)
cv2.imshow("img_open", img_open)
cv2.imshow("img_close", img_close)
cv2.imshow("img_gradient", img_gradient)
cv2.waitKey(0)
cv2.destroyAllWindows()
