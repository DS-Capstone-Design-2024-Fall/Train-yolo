from ultralytics import YOLO, settings
import pandas as pd
import numpy as np

settings["datasets_dir"] = "/data/fehs0611/datasets"
settings.update()

# Load a pre-trained YOLO model
# model = YOLO("../train/runs/detect/train242/weights/best.pt")
# model = YOLO("../train/results/v8m-result-ds3-balanced/weights/best.pt")
# model = YOLO("../train/results/v8m-result-4/weights/best.pt")
# model = YOLO("../train/results/v11m-result-5-tuned/weights/best.pt")
# model = YOLO("../train/results/v11m-result-5-tuned-db/weights/best.pt")
model = YOLO("../train/results/v11m-result-5-tuned-db-1000/weights/best.pt")

path = "test.yaml"
results = model.val(
    data=path,
    save_json=True,  # 결과 json 저장
    split="test",  # 검증을 위해 사용되는 데이터셋 분할
    # save_hybrid=True,  # 라벨 + 예측값 -> 미구현된 기능인지 True/False 똑같음 (https://github.com/ultralytics/ultralytics/issues/11698
)

#   0: braille-block-defect
#   1: sidewalk-block-defect
#   2: bicycle-road-defect
matrix = np.array(
    [
        results.mean_results(),
        results.class_result(0),
        results.class_result(1),
        results.class_result(2),
    ]
)

df = pd.DataFrame(
    matrix,
    columns=["Precision(B)", "Recall(B)", "AP50(B)", "AP50-95"],
    index=[
        "All (mean)",
        "Braille-block-defect",
        "Sidewalk-block-defect",
        "Bicycle-road-defect",
    ],
)

df.to_csv("result.csv", index=True, encoding="utf-8")
