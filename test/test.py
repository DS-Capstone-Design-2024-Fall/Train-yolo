from ultralytics import YOLO, settings

# yolo settings datasets_dir='/data/fehs0611/datasets/'
settings["datasets_dir"] = "/data/fehs0611/datasets/"
settings.update()

# Load a COCO-pretrained YOLOv5n model
# model = YOLO("yolov8n.pt")
model = YOLO("../train/v8n-pretraining-result/weights/best.pt")

path = "../street-facilities.yaml"
results = model.val(data=path)
