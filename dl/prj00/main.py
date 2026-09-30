from ultralytics import YOLO

#model 학습 데이터 불러오기
# m = YOLO("yolov8n.pt")
m = YOLO("./runs/detect/train/weights/best.pt")

#학습 : best.pt 얻을 수 있음
# m.train(data="./prj20260911.v1i.yolov8/data.yaml", epochs=100, imgsz=640)

# m(
#     "https://www.sciencetimes.co.kr/jnrepo/uploads/2019/02/800px-Zebra_Botswana_edit02.jpg",
#     save=True,
#     project="D:/dev/dl/prj00/runs",  # prj00 폴더 아래에 runs가 생기도록 지정
#     name="predict",
# )
# 예측
m("./abc.png",save=True)
