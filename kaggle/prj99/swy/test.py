from ultralytics import YOLO

m = YOLO("yolov8n.pt")
result = m("https://cdn.iusm.co.kr/news/photo/202401/1031696_580507_104.jpg" ,save=True)