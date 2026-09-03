import cv2

# img = cv2.imread("images/image1.png")
#
# print(img)
#
# cv2.imshow("image", img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# cv2.imwrite("images/result.png", img)


# === 비디오 파일 다루기 ===
cap = cv2.VideoCapture("videos/0.mp4")
fps = cap.get(cv2.CAP_PROP_FPS)
w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

fourcc = cv2.VideoWriter_fourcc(*"mp4v")
out = cv2.VideoWriter('videos/result.mp4', fourcc, fps, (w, h))

delay = int(1000 / fps)
while True:
    is_read, frame = cap.read()
    if not is_read: break

    out.write(frame)
    cv2.imshow("frame", frame)
    cv2.waitKey(delay)

out.release()
cap.release()
cv2.destroyAllWindows()