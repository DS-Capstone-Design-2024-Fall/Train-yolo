from ultralytics import YOLO, settings

settings["datasets_dir"] = "/data/fehs0611/datasets/"
settings.update()

# model = YOLO("yolov8m.pt")
model = YOLO("yolo11m.pt")

path = "../street-facilities.yaml"
results = model.tune(
    data=path,
    epochs=50,
    iterations=100,
    imgsz=640,
    optimizer="AdamW",
    single_cls=True,
)
