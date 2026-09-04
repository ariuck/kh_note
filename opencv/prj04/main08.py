# # 경계 , 엣지

# === sobel ===
# import cv2
#
# img = cv2.imread("images/roi.jpg",cv2.IMREAD_GRAYSCALE)
# img = cv2.resize(img, (500,700))
#
# img_blur = cv2.GaussianBlur(img,(5,5),0)
#
#
# # sobel
# sobel_x = cv2.Sobel(img_blur, cv2.CV_64F,1,0,ksize=3)
# sobel_y = cv2.Sobel(img_blur, cv2.CV_64F,0,1,ksize=3)
##절대값
# sobel_x = cv2.convertScaleAbs(sobel_x)
# sobel_y = cv2.convertScaleAbs(sobel_y)
#
# sobel_xy = cv2.addWeighted(sobel_x,0.5,sobel_y,0.5,0)
# cv2.imshow("img", img)
# cv2.imshow("img_blur", img_blur)
# cv2.imshow("sobel_x", sobel_x)
# cv2.imshow("sobel_y", sobel_y)
# cv2.imshow("sobel_xxy", sobel_xy)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# import cv2
# # === Laplacian ===
# img = cv2.imread("images/roi.jpg", cv2.IMREAD_GRAYSCALE)
# img = cv2.resize(img, (500,700))
# img = cv2.GaussianBlur(img, (5,5), 0)
#
# result = cv2.Laplacian(img, cv2.CV_64F)
# result = cv2.convertScaleAbs(result)
#
#
# cv2.imshow("img", img)
# cv2.imshow("result", result)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

import cv2
# ===Canny === (실질적으로 이걸 제일 많이쓰고 이거만 쓸듯)
img = cv2.imread("images/roi.jpg", cv2.IMREAD_GRAYSCALE)
img = cv2.resize(img, (500,700))
img = cv2.GaussianBlur(img, (5,5), 0)

result = cv2.Canny(img, 50, 100)

cv2.imshow("img", img)
cv2.imshow("result", result)
cv2.waitKey(0)
cv2.destroyAllWindows()