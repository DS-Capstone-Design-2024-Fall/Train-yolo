from ultralytics import YOLO, settings

# yolo settings datasets_dir='/data/fehs0611/datasets/'
settings["datasets_dir"] = "/data/fehs0611/datasets/"
settings.update()

# Load a COCO-pretrained YOLOv5n model
model = YOLO("../train/v8m-result-ds3-balanced/weights/best.pt")

path = "test.yaml"
results = model.val(
    data=path,
    save_json=True,  # 결과 json 저장
    split="test",  # 검증을 위해 사용되는 데이터셋 분할
    save_hybrid=True,  # 라벨 + 예측값
)
