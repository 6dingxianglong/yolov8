from ultralytics import YOLO

# Load a model
model = YOLO("birds_type.pt")  # load a pretrained model (recommended for training)

model.predict(
    source = "https://youtu.be/15YLOlkC1co?si=DkSyZUYfn10RQwxb",
    conf = 0.5,
    save = True, 
    save_txt = True,
    save_conf = True,
    save_crop = True,
    visualize = False,

)



