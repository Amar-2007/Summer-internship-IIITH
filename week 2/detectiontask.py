from ultralytics import YOLO

model = YOLO("yolo26n.pt")

results = model("https://ultralytics.com/images/bus.jpg")

results[0].show()
