from ultralytics import YOLO

if __name__ == '__main__':
    model = YOLO('yolo26n.pt')

    model.train(
        data='dataset/data.yaml',
        epochs=3,
        imgsz=(640,640),
        batch=16,
        name="kh_detector"
    )

