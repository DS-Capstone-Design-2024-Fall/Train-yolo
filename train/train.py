from ultralytics import YOLO, settings

settings["datasets_dir"] = "/data/fehs0611/datasets/"
settings.update()

# Load a COCO-pretrained YOLOv5n model
model = YOLO("yolov8m.pt")
# model = YOLO("./v8n-pretraining-result/weights/best.pt")

path = "../street-facilities.yaml"
results = model.train(
    data=path,
    epochs=120,
    imgsz=640,
    # hyp="best_hyperparameters.yaml",
    hyp="args.yaml",
)
