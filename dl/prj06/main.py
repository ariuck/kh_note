from pathlib import Path

from ultralytics import YOLO

x = Path(__file__).resolve().parent

model = YOLO("best.pt")

result = model(
    "test_images",
    save = True,
    conf=0.5,
    project = f"{x}/PPPP",
    name = "nameeeee")
