from ultralytics import YOLO
from ultralytics_platform.resources import projects

model = YOLO("best.pt")

result = model(
    "test_images",
    save = True,
    conf=0.5,
    project = "/dev/dl/prj06/projecttttt",
    name = "nameeeee")
