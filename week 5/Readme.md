This task demonstrates object detection using the YOLO (You Only Look Once) model. A pre-trained YOLO model was fine-tuned on a custom dataset to detect specific classes. The trained model was then used to perform inference on unseen test frames extracted from a video, and the results were saved with bounding boxes.

Inference (Object Detection) Inference was performed using the trained weights: from ultralytics import YOLO model = YOLO("runs/detect/train/weights/best.pt") model.predict( source="testing", save=True, conf=0.25)

Output Results: Each image contains: Bounding boxes Class labels Confidence scores
