from ultralytics import YOLO, settings

# yolo settings datasets_dir='/data/fehs0611/datasets/'
settings["datasets_dir"] = "/data/fehs0611/datasets/"
settings.update()

# Load a COCO-pretrained YOLOv5n model
model = YOLO("yolov8n.pt")
# model = YOLO("./v8n-pretraining-result/weights/best.pt")

# Display model information (optional)
# model.info()

path = "../street-facilities.yaml"
results = model.train(
    data=path,
    epochs=500,
    imgsz=640,
    device=[0],  # use one cuda device
)
