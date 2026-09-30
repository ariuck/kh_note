from ultralytics import YOLO

model = YOLO('best.pt')
results = model('test_images' , conf=0.635 , save=True , project="D:/본인이 원하는 경로/runs/detect")

for r in results:
    print(r.to_json())

