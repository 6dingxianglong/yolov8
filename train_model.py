from ultralytics import YOLO

# Load a model
model = YOLO("yolov8n.pt")  # load a pretrained model (recommended for training)

result = model.train(
    # device="mps",
    data="coco.yaml",
    imgsz=256,
    epochs=200,
    patience=50,
    batch=10,
    project='yolov8_results',
    name='v4'
)