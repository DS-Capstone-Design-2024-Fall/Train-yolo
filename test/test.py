from ultralytics import YOLO, settings

# yolo settings datasets_dir='/data/fehs0611/datasets/'
settings["datasets_dir"] = "/data/fehs0611/datasets/"
settings.update()

# Load a COCO-pretrained YOLOv5n model
model = YOLO("../train/v8n-result-3-balanced/weights/best.pt")
# model = YOLO("../train/v8n-result-2-only0/weights/best.pt")

path = "test.yaml"
results = model.val(data=path)
