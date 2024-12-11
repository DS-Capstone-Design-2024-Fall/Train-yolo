import warnings
from ultralytics import settings
import os
import numpy as np
import cv2


# 정답 라벨에 대한 bbox 시각화
def visualize_bbox(
    image,
    bboxes,  # class, x, y, width, height -> Normalized form
    bgr: tuple = (0, 0, 255),  # bbox 테두리 색, BGR
    thickness: int = 2,
    #    save_path : os.path = None, # 파일명까지 포함해야 함
):
    h, w, _ = image.shape
    for bbox in bboxes:
        # bbox 정보
        class_type = bbox[0]
        xcenter, ycenter, width, height = bbox[1:]
        xmin, xmax = xcenter - width / 2, xcenter + width / 2
        ymin, ymax = ycenter - height / 2, ycenter + height / 2

        # bbox 그리기
        pt1 = np.int16(np.ceil([xmin * w, ymin * h]))
        pt2 = np.int16(np.ceil([xmax * w, ymax * h]))
        image = cv2.rectangle(image, pt1, pt2, bgr, thickness)

    return image


# 정답 라벨
# GPU server environment
settings["datasets_dir"] = "/data/fehs0611/datasets"
settings.update()
datasets_dir = settings["datasets_dir"]
# label_dir = f"{datasets_dir}/street-facilities-3/labels/test"
label_dir = f"{datasets_dir}/street-facilities-5-db/labels/test"

# Local PC environment
# label_dir = f"D:/Downloads/street-facilities-3/labels/test"

# bbox 추가하기 전 이미지 -> test 이미지에 대해 prediction 을 거친 이미지들을 사용 (예측bbox 표시됨)
img_path = "./prediction-images"
# bbox 추가 후 저장 경로
img_dest_path = "./prediction-images-with-ans"

images = [f for f in os.listdir(img_path)]

os.makedirs(img_dest_path, exist_ok=True)  # 이미 있는 폴더면 생성 x

n = len(images)
for i, image in enumerate(images):
    # if i % 100 == 0: print(f"{i+1} / {n}")
    fname = os.path.splitext(image)[0]
    bboxes = []

    # load original image
    cv2_image = cv2.imread(
        os.path.join(img_path, image), cv2.IMREAD_COLOR
    )  # 컬러이미지

    # load label data
    # 경고 무시
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", category=UserWarning)

        label = os.path.join(label_dir, fname) + ".txt"
        with open(label, "r") as file:
            for line in file:
                # 각 줄을 공백 기준으로 나누고 float 변환
                bbox = np.array([float(value) for value in line.strip().split()])
                bboxes.append(bbox)

    save_path = os.path.join(img_dest_path, image)
    cv2_image = visualize_bbox(cv2_image, bboxes)
    # 이미지 저장
    if save_path:
        try:
            cv2.imwrite(save_path, cv2_image)
        except Exception as e:
            print(f"failed to save the image ({save_path}): {e}")
