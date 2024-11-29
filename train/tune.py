from ultralytics import YOLO, settings
import os
from torch.utils.data import DataLoader

settings["datasets_dir"] = "/data/fehs0611/datasets/"
settings.update()

model = YOLO("yolov8m.pt")
# model = YOLO("./v8n-pretraining-result/weights/best.pt")

num_workers = os.cpu_count()  # now available cpu workers(core)
print("num workers", num_workers)

path = "../street-facilities.yaml"
results = model.tune(
    workers=num_workers,
    data=path,
    epochs=30,
    iterations=10,
    imgsz=640,
    optimizer="AdamW",
    cos_lr=True,
    device=[0],  # use one cuda device
)
