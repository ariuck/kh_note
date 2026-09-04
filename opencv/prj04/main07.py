# #필터링, 블러링
#
# import cv2
# import numpy as np
#
# img = cv2.imread("images/48.jpg")
# img = cv2.resize(img, (500, 500))
#
# img_blur = cv2.blur(img, (5,5))
# img_blur_g = cv2.GaussianBlur(img, (5,5), 1)
# img_blur_m = cv2.medianBlur(img,5)
# img_blur_b = cv2.bilateralFilter(img,5,100,100)
#
# k = kernel = np.array([[ 0, -1,  0],
#                    [-1,  5, -1],
#                    [ 0, -1,  0]])
# img_k = cv2.filter2D(img,-1,k)
#
# cv2.imshow("img", img)
# cv2.imshow("img_blur", img_blur)
# cv2.imshow("img_blur_g", img_blur_g)
# cv2.imshow("img_blur_m", img_blur_m)
# cv2.imshow("img_blur_b", img_blur_b)
# cv2.imshow("img_k", img_k)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
import cv2
import numpy as np

#=== 노이즈 제거===
rng = np.random.default_rng(42)
img = np.full((500,500),128,dtype="uint8")
xs = rng.integers(0,500,3000)
ys = rng.integers(0,500,3000)
noise = rng.integers(0,2,3000)
img[ys,xs] = np.where(noise,0,255)

img_blur = cv2.medianBlur(img,25,25)
img_blur_m = cv2.medianBlur(img,25)
img_blur_g = cv2.GaussianBlur(img,(25,25),0)

cv2.imshow("img",img)
cv2.imshow("img_blur",img_blur)
cv2.imshow("img_blur_m",img_blur_m)
cv2.imshow("img_blur_g",img_blur_g)
cv2.waitKey(0)
cv2.destroyAllWindows()