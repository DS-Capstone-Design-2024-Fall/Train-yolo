from ultralytics import YOLO, settings

settings["datasets_dir"] = "/data/fehs0611/datasets/"
settings.update()

# Load a COCO-pretrained YOLOv5n model
# model = YOLO("yolo11m.pt")
# model = YOLO("yolov8m.pt")
# model = YOLO("./v8n-pretraining-result/weights/best.pt")

path = "../street-facilities.yaml"
# results = model.train(
#     data=path,
#     epochs=500,
#     imgsz=640,
#     cfg="./results/v11m-tune/best_hyperparameters.yaml",
#     # cfg="args.yaml",
# )


# model = YOLO("./results/v11m-result-5-tuned-db/weights/best.pt")  # 추가 학습

# results = model.train(
#     data=path,
#     epochs=1000,
#     imgsz=640,
#     cfg="./results/v11m-result-5-tuned-db/args.yaml",
#     optimizer="SGD",  # 기본값인 "Auto" 사용 시 lr0, lrf 값 무시됨. 어차피 1만회 이상 반복에서는 Auto 에서 SGD 선택.
#     lr0=0.0005,
#     lrf=0.01,
# )


# model = YOLO("./savepoint/v11m-5-db-plus/weights/last.pt")  # 학습재개
model = YOLO("./savepoint/v11m-5-db-966/weights/last.pt")  # 학습재개
model.train(resume=True)
