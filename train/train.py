from ultralytics import YOLO, settings

# yolo settings datasets_dir='/data/fehs0611/datasets/'
settings["datasets_dir"] = "/data/fehs0611/datasets/"
settings.update()

# Load a COCO-pretrained YOLOv5n model
model = YOLO("yolov8m.pt")
# model = YOLO("./v8n-pretraining-result/weights/best.pt")

# Display model information (optional)
# model.info()

# memo
# optimizer: 'optimizer=auto' found, ignoring 'lr0=0.01' and 'momentum=0.937'
# and determining best 'optimizer', 'lr0' and 'momentum' automatically...
# SGD(lr=0.01, momentum=0.9)


path = "../street-facilities.yaml"
results = model.train(
    data=path,
    epochs=400,
    imgsz=640,
    hyp="best_hyperparameters.yaml",
    device=[0],  # use one cuda device
)
