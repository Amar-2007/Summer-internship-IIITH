# Custom Dataset & YAML Explanation

This dataset was created using Label Studio.

Dataset contains:

* 3 classes → car, van, truck
* Images labeled manually using bounding boxes

YOLO label format:
<class_id> <x_center> <y_center> <width> <height>

Values are normalized between 0 and 1.

data.yaml contains:

* dataset path
* train and validation split
* class names mapping
