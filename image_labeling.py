import os
import cv2


image_folder = r"C:\\Users\\crack\\2"  
label_folder = r"C:\\Users\\label"  


image_files = [f for f in os.listdir(image_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]

# 고정 클래스 ID
class_id = 0

# 윈도우 크기 설정
window_width = 800
window_height = 600


for file_index, file_name in enumerate(image_files):
 
    image_path = os.path.join(image_folder, file_name)

  
    image = cv2.imread(image_path)
    if image is None:
        continue

    # 이미지 크기 조정
    height, width, _ = image.shape
    aspect_ratio = width / height
    if aspect_ratio > 1:
        resized_width = window_width
        resized_height = int(window_width / aspect_ratio)
    else:
        resized_height = window_height
        resized_width = int(window_height * aspect_ratio)
    resized_image = cv2.resize(image, (resized_width, resized_height))

    # 이미지 출력
    cv2.imshow("Image", resized_image)
    print(f"[{file_index + 1}/{len(image_files)}] 처리 중인 이미지: {file_name}")

    # ROI(Bounding Box) 선택
    roi = cv2.selectROI("Image", resized_image, fromCenter=False, showCrosshair=True)
    x, y, w, h = roi

    if w == 0 or h == 0:
        cv2.destroyAllWindows()
        continue

    x = int(x * width / resized_width)
    y = int(y * height / resized_height)
    w = int(w * width / resized_width)
    h = int(h * height / resized_height)

    x_center = (x + w / 2) / width
    y_center = (y + h / 2) / height
    box_width = w / width
    box_height = h / height

    txt_file_name = os.path.splitext(file_name)[0] + ".txt"
    label_path = os.path.join(label_folder, txt_file_name)

    # 라벨 저장 (YOLO 형식: class_id x_center y_center width height)
    with open(label_path, "w") as f:
        f.write(f"{class_id} {x_center:.6f} {y_center:.6f} {box_width:.6f} {box_height:.6f}\n")

    cv2.destroyAllWindows()

