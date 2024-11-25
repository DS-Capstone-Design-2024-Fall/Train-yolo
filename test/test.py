from ultralytics import YOLO, settings
import pandas as pd

# yolo settings datasets_dir='/data/fehs0611/datasets/'
settings["datasets_dir"] = "/data/fehs0611/datasets"
settings.update()

# Load a pre-trained YOLO model
model = YOLO("../train/v8m-result-ds3-balanced/weights/best.pt")

path = "test.yaml"
results = model.val(
    data=path,
    save_json=True,  # 결과 json 저장
    split="test",  # 검증을 위해 사용되는 데이터셋 분할
    # save_hybrid=True,  # 라벨 + 예측값 -> 미구현된 기능인지 True/False 똑같음 (https://github.com/ultralytics/ultralytics/issues/11698
)

# test 결과 성능
# map5095 = results.box.map
# map50 = results.box.map50
# map75 = results.box.map75

# data = {"mAP@0.5:0.95": [map5095], "mAP@0.5": [map50], "mAP@0.75": [map75]}

# # Create a DataFrame
# df = pd.DataFrame(data)

# # Save the DataFrame to a CSV file
# df.to_csv("map_results.csv", index=False)

print(results.box.maps)

# df = pd.DataFrame(results.box.maps)
