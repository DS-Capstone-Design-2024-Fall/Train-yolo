from ultralytics import YOLO, settings

# yolo settings datasets_dir='/data/fehs0611/datasets/'
settings["datasets_dir"] = "/data/fehs0611/datasets/"
settings.update()

# Load a COCO-pretrained YOLOv5n model
model = YOLO("yolov8n.pt")

# Display model information (optional)
model.info()

path = "../crack-pretraining.yaml"
results = model.train(
    data=path,
    epochs=100,
    imgsz=640,
    device=[0],  # use one cuda device
)
