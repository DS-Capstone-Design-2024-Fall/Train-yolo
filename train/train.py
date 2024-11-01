from ultralytics import YOLO

# Load a COCO-pretrained YOLOv5n model
model = YOLO("yolov8n.pt")

# Display model information (optional)
model.info()

path = "../street-facilities.yaml"
results = model.train(
    data=path, epochs=100, imgsz=640, device=[0]  # use one cuda device
)
