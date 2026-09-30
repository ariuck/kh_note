# OpenCV
# 픽셀 , 해상도 , 8bit , 채널(흑백,컬러)
# RGB , BGR , GrayScale , HSV , YCrCb
# shape : 너비 높이 (행렬은 행,열 반대 주의)
import cv2

# imread("~~~")
# imshow()
img = cv2.imread("~~~")
if img is None:
    raise ValueError("Could not load image")
'''
cv2.imshow()
cv2.waitKey(0)
cv2.destroyAllWindows()
'''

# cv2.imwrite()

# ROI 추출