## Yolov8s

## 1. Specification of dependencies
```bash
git clone https://github.com/hasibzunair/bdss20k-dataset.git
cd bdss20k-dataset/object_detectors/yolov8s
conda create -n yolo8s python=3.8 -y
conda activate yolo8s
pip install ultralytics
```

## 2. Dataset
The class list for this task is:

```bash
# classes.txt
person
rickshaw
rickshaw van
auto rickshaw
truck
pickup truck
private car
motorcycle
bicycle
bus
micro bus
covered van
human hauler
```

**Dataset statistics**:

| Name     | Number of images/label pairs |
| -------- | ---------------------------- |
| `train`  | 3,985                        |
| `val`    | 1004                         |
| `test`   | 649                          |
| `pseudo` | 14,762                       |

Open a new folder named `datasets` and keep it under `object_detectors/` folder. Our project utilizes two prominent data formats: COCO and YOLO. The YOLO format is specifically employed for the Yolov8 variants (l, s, m), while the COCO format is adopted for the rtmdet and detr models. For an in-depth understanding of these formats, explore the COCO format [here](https://roboflow.com/formats/coco-json) and the YOLO format [here](https://roboflow.com/formats/yolov8-pytorch-txt). 


## 3. Training and Evaluation

To train a YOLOv8s model, first download the pretrained model from [here](https://github.com/hasibzunair/bdss20k-dataset/releases/download/0.0.1/best.pt) and put them in `yolov8s/runs/detect/train/weights/` folder. Then run:

```bash
python train.py --yaml_path ./data/bdss20k.yaml --batch_size 12 --epochs 400 --device 0
```
Evaluate model on validation or test set. Model checkpoints are saved in yolov8s/runs folder.

```bash
python test.py --weights ./runs/detect/train/weights/best.pt --yaml_path ./data/bdss20k.yaml --batch_size 12 --device 0 
```

Make predictions on set of images.
```bash
python infer.py --weights ./runs/detect/train/weights/best.pt --test_image_path ../datasets/bdss20k/images/test/ --save_dir predictions/
```


## 4. Results

#### Validation Results
| Class         | Images | Instances | Box(P) | R     | mAP50 | mAP50-95 |
| ------------- | ------ | --------- | ------ | ----- | ----- | -------- |
| all           | 1004   | 7385      | 0.804  | 0.691 | 0.784 | 0.637    |
| person        | 1004   | 1917      | 0.896  | 0.756 | 0.883 | 0.645    |
| rickshaw      | 1004   | 1587      | 0.894  | 0.825 | 0.910 | 0.765    |
| rickshaw van  | 1004   | 240       | 0.778  | 0.667 | 0.736 | 0.482    |
| auto rickshaw | 1004   | 590       | 0.914  | 0.880 | 0.932 | 0.809    |
| truck         | 1004   | 65        | 0.636  | 0.592 | 0.668 | 0.569    |
| pickup truck  | 1004   | 74        | 0.720  | 0.676 | 0.745 | 0.578    |
| private car   | 1004   | 1420      | 0.888  | 0.806 | 0.904 | 0.771    |
| motorcycle    | 1004   | 860       | 0.896  | 0.801 | 0.904 | 0.689    |
| bicycle       | 1004   | 146       | 0.775  | 0.541 | 0.681 | 0.493    |
| bus           | 1004   | 182       | 0.831  | 0.675 | 0.801 | 0.687    |
| micro bus     | 1004   | 241       | 0.758  | 0.602 | 0.742 | 0.680    |
| covered van   | 1004   | 40        | 0.787  | 0.556 | 0.641 | 0.561    |
| human hauler  | 1004   | 23        | 0.682  | 0.609 | 0.642 | 0.552    |

#### Test Result
| Class         | Images | Instances | Box(P) | R     | mAP50 | mAP50-95 |
| ------------- | ------ | --------- | ------ | ----- | ----- | -------- |
| all           | 649    | 3805      | 0.800  | 0.754 | 0.844 | 0.694    |
| person        | 649    | 844       | 0.833  | 0.819 | 0.898 | 0.702    |
| rickshaw      | 649    | 1129      | 0.854  | 0.918 | 0.963 | 0.860    |
| rickshaw van  | 649    | 83        | 0.709  | 0.747 | 0.767 | 0.528    |
| auto rickshaw | 649    | 228       | 0.891  | 0.939 | 0.964 | 0.872    |
| truck         | 649    | 29        | 0.637  | 0.586 | 0.606 | 0.500    |
| pickup truck  | 649    | 65        | 0.861  | 0.723 | 0.851 | 0.594    |
| private car   | 649    | 543       | 0.839  | 0.915 | 0.960 | 0.865    |
| motorcycle    | 649    | 509       | 0.878  | 0.886 | 0.957 | 0.751    |
| bicycle       | 649    | 121       | 0.803  | 0.776 | 0.893 | 0.694    |
| bus           | 649    | 86        | 0.773  | 0.674 | 0.826 | 0.651    |
| micro bus     | 649    | 105       | 0.901  | 0.562 | 0.834 | 0.768    |
| covered van   | 649    | 24        | 0.681  | 0.458 | 0.611 | 0.535    |
| human hauler  | 649    | 39        | 0.736  | 0.795 | 0.836 | 0.707    |


## 5. Pre-trained models
We provide pretrained models on GitHub Releases for reproducibility. Download the model from [Here](https://github.com/hasibzunair/bdss20k-dataset/releases/download/0.0.1/best.pt).

##### Acknowledgement

This codebase havily build on [ultralytics](https://github.com/ultralytics/ultralytics)



### Extra
<details>
  <summary> Validation Results</summary>

| Class         | Images | Instances | Box(P) | R     | mAP50 | mAP50-95 |
| ------------- | ------ | --------- | ------ | ----- | ----- | -------- |
| all           | 1004   | 7385      | 0.804  | 0.691 | 0.784 | 0.637    |
| person        | 1004   | 1917      | 0.896  | 0.756 | 0.883 | 0.645    |
| rickshaw      | 1004   | 1587      | 0.894  | 0.825 | 0.910 | 0.765    |
| rickshaw van  | 1004   | 240       | 0.778  | 0.667 | 0.736 | 0.482    |
| auto rickshaw | 1004   | 590       | 0.914  | 0.880 | 0.932 | 0.809    |
| truck         | 1004   | 65        | 0.636  | 0.592 | 0.668 | 0.569    |
| pickup truck  | 1004   | 74        | 0.720  | 0.676 | 0.745 | 0.578    |
| private car   | 1004   | 1420      | 0.888  | 0.806 | 0.904 | 0.771    |
| motorcycle    | 1004   | 860       | 0.896  | 0.801 | 0.904 | 0.689    |
| bicycle       | 1004   | 146       | 0.775  | 0.541 | 0.681 | 0.493    |
| bus           | 1004   | 182       | 0.831  | 0.675 | 0.801 | 0.687    |
| micro bus     | 1004   | 241       | 0.758  | 0.602 | 0.742 | 0.680    |
| covered van   | 1004   | 40        | 0.787  | 0.556 | 0.641 | 0.561    |
| human hauler  | 1004   | 23        | 0.682  | 0.609 | 0.642 | 0.552    |

</details>

<details>
  <summary>Test Results</summary>

| Class         | Images | Instances | Box(P) | R     | mAP50 | mAP50-95 |
| ------------- | ------ | --------- | ------ | ----- | ----- | -------- |
| all           | 649    | 3805      | 0.800  | 0.754 | 0.844 | 0.694    |
| person        | 649    | 844       | 0.833  | 0.819 | 0.898 | 0.702    |
| rickshaw      | 649    | 1129      | 0.854  | 0.918 | 0.963 | 0.860    |
| rickshaw van  | 649    | 83        | 0.709  | 0.747 | 0.767 | 0.528    |
| auto rickshaw | 649    | 228       | 0.891  | 0.939 | 0.964 | 0.872    |
| truck         | 649    | 29        | 0.637  | 0.586 | 0.606 | 0.500    |
| pickup truck  | 649    | 65        | 0.861  | 0.723 | 0.851 | 0.594    |
| private car   | 649    | 543       | 0.839  | 0.915 | 0.960 | 0.865    |
| motorcycle    | 649    | 509       | 0.878  | 0.886 | 0.957 | 0.751    |
| bicycle       | 649    | 121       | 0.803  | 0.776 | 0.893 | 0.694    |
| bus           | 649    | 86        | 0.773  | 0.674 | 0.826 | 0.651    |
| micro bus     | 649    | 105       | 0.901  | 0.562 | 0.834 | 0.768    |
| covered van   | 649    | 24        | 0.681  | 0.458 | 0.611 | 0.535    |
| human hauler  | 649    | 39        | 0.736  | 0.795 | 0.836 | 0.707    |

</details>


