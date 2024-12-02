from ultralytics import YOLO, settings

settings["datasets_dir"] = "/data/fehs0611/datasets/"
settings.update()

# Load a COCO-pretrained YOLOv5n model
model = YOLO("yolo11m.pt")
# model = YOLO("yolov8m.pt")
# model = YOLO("./v8n-pretraining-result/weights/best.pt")

path = "../street-facilities.yaml"
results = model.train(
    data=path,
    epochs=500,
    imgsz=640,
    cfg="./v11m-tune/best_hyperparameters.yaml",
    # cfg="args.yaml",
)
