from ultralytics import YOLO, settings
from PIL import Image
import os
import gc
from pathlib import Path

# Load a pre-trained YOLO model
model = YOLO("../train/v8m-result-ds3-balanced/weights/best.pt")


# GPU server environment
# # yolo settings datasets_dir='/data/fehs0611/datasets/'
settings["datasets_dir"] = "/data/fehs0611/datasets"
settings.update()
dataset_dir = settings["datasets_dir"]
path = f"{dataset_dir}/street-facilities-3/images/test"

# Local PC enviroment
# path = f"D:/Downloads/street-facilities-3/images/test"

dpath = f"./prediction-images"

images = [f for f in os.listdir(path)]

os.makedirs(dpath, exist_ok=True)

# os 에서 open files 갯수 제한이 있으므로 제한 갯수 내의 파일을 한 묶음으로 처리
# ulimit -a
batch_size = 512
for i in range(0, len(images) + batch_size, batch_size):
    end = min(i + batch_size, len(images))
    batch = images[i:end]
    results = model.predict([os.path.join(path, f) for f in batch])

    for j, r in enumerate(results):
        # Plot results
        im_bgr = r.plot()
        im_rgb = Image.fromarray(im_bgr[..., ::-1])
        im_rgb.save(f"{dpath}/{Path(r.path).name}")
        del im_rgb  # Delete object
    gc.collect()  # Force garbage collection
