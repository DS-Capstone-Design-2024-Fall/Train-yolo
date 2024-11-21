from ultralytics import YOLO

# Load a model
model = YOLO("./v8m-result-ds3-balanced/weights/best.pt")  # load a custom trained model

# Export the model
model.export(format="tflite")
