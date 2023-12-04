## Yolov8l

## 1. Specification of dependencies
```bash
git clone https://github.com/hasibzunair/bdss20k-dataset.git
cd bdss20k-dataset/object_detectors/yolov8m
conda create -n yolo8l python=3.8 -y
conda activate yolo8l
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

To train YOLOv8l model, first download the pretrained model from [here](https://github.com/hasibzunair/bdss20k-dataset/releases/download/0.0.3/best.pt) and put them in `yolov8m/runs/detect/train/weights/` folder. Then run:

```bash
python train.py --yaml_path ./data/bdss20k.yaml --batch_size 12 --epochs 400 --device 0
```
Evaluate model on validation or test set. Model checkpoints are saved in yolov8m/runs folder.

```bash
python test.py --weights ./runs/detect/train/weights/best.pt --yaml_path ./data/bdss20k.yaml --batch_size 12 --device 0 
```

Make predictions on set of images.
```bash
python infer.py --weights ./runs/detect/train/weights/best.pt --test_image_path ../datasets/bdss20k/images/test/ --save_dir predictions/
```


## 4. Results

#### Validation

| Class          | Images | Instances | Box(P) | R    | mAP50 | mAP50-95 |
|----------------|--------|-----------|--------|------|-------|----------|
| all            | 1004   | 7385      | 0.805  | 0.734| 0.814 | 0.675    |
| person         | 1004   | 1917      | 0.875  | 0.806| 0.903 | 0.676    |
| rickshaw       | 1004   | 1587      | 0.873  | 0.857| 0.927 | 0.79     |
| rickshaw van   | 1004   | 240       | 0.775  | 0.775| 0.799 | 0.53     |
| auto rickshaw  | 1004   | 590       | 0.91   | 0.893| 0.946 | 0.829    |
| truck          | 1004   | 65        | 0.712  | 0.57 | 0.729 | 0.64     |
| pickup truck   | 1004   | 74        | 0.736  | 0.715| 0.778 | 0.635    |
| private car    | 1004   | 1420      | 0.887  | 0.825| 0.921 | 0.805    |
| motorcycle     | 1004   | 860       | 0.898  | 0.849| 0.925 | 0.72     |
| bicycle        | 1004   | 146       | 0.717  | 0.664| 0.724 | 0.552    |
| bus            | 1004   | 182       | 0.816  | 0.775| 0.86  | 0.745    |
| micro bus      | 1004   | 241       | 0.769  | 0.636| 0.748 | 0.696    |
| covered van    | 1004   | 40        | 0.7    | 0.525| 0.628 | 0.569    |

#### Testing

| Class          | Images | Instances | Box(P) | R     | mAP50 | mAP50-95 |
|----------------|--------|-----------|--------|-------|-------|----------|
| all            | 649    | 3805      | 0.762  | 0.806 | 0.832 | 0.704      |
| person         | 649    | 844       | 0.781  | 0.879 | 0.908 | 0.736    |
| rickshaw       | 649    | 1129      | 0.848  | 0.944 | 0.969 | 0.883    |
| rickshaw van   | 649    | 83        | 0.63   | 0.656 | 0.672 | 0.474    |
| auto rickshaw  | 649    | 228       | 0.878  | 0.908 | 0.957 | 0.885    |
| truck          | 649    | 29        | 0.533  | 0.513 | 0.417 | 0.348    |
| pickup truck   | 649    | 65        | 0.819  | 0.846 | 0.902 | 0.679    |
| private car    | 649    | 543       | 0.84   | 0.932 | 0.959 | 0.879    |
| motorcycle     | 649    | 509       | 0.845  | 0.929 | 0.959 | 0.771    |
| bicycle        | 649    | 121       | 0.802  | 0.868 | 0.902 | 0.731    |
| bus            | 649    | 86        | 0.768  | 0.731 | 0.812 | 0.641    |
| micro bus      | 649    | 105       | 0.892  | 0.886 | 0.929 | 0.867    |
| covered van    | 649    | 24        | 0.614  | 0.542 | 0.61  | 0.535    |
| human hauler   | 649    | 39        | 0.653  | 0.846 | 0.823 | 0.671    |

## 5. Pre-trained models
We provide pretrained models on GitHub Releases for reproducibility. Download the model from [Here](https://github.com/hasibzunair/bdss20k-dataset/releases/download/0.0.3/best.pt).

## Acknowledgement

This codebase havily build on [ultralytics](https://github.com/ultralytics/ultralytics).


#### Extra

<details>
  <summary>Validation Results</summary>

| Class          | Images | Instances | Box(P) | R    | mAP50 | mAP50-95 |
|----------------|--------|-----------|--------|------|-------|----------|
| all            | 1004   | 7385      | 0.805  | 0.734| 0.814 | 0.675    |
| person         | 1004   | 1917      | 0.875  | 0.806| 0.903 | 0.676    |
| rickshaw       | 1004   | 1587      | 0.873  | 0.857| 0.927 | 0.79     |
| rickshaw van   | 1004   | 240       | 0.775  | 0.775| 0.799 | 0.53     |
| auto rickshaw  | 1004   | 590       | 0.91   | 0.893| 0.946 | 0.829    |
| truck          | 1004   | 65        | 0.712  | 0.57 | 0.729 | 0.64     |
| pickup truck   | 1004   | 74        | 0.736  | 0.715| 0.778 | 0.635    |
| private car    | 1004   | 1420      | 0.887  | 0.825| 0.921 | 0.805    |
| motorcycle     | 1004   | 860       | 0.898  | 0.849| 0.925 | 0.72     |
| bicycle        | 1004   | 146       | 0.717  | 0.664| 0.724 | 0.552    |
| bus            | 1004   | 182       | 0.816  | 0.775| 0.86  | 0.745    |
| micro bus      | 1004   | 241       | 0.769  | 0.636| 0.748 | 0.696    |
| covered van    | 1004   | 40        | 0.7    | 0.525| 0.628 | 0.569    |
</details>

<details>
  <summary>Test Results</summary>

| Class          | Images | Instances | Box(P) | R     | mAP50 | mAP50-95 |
|----------------|--------|-----------|--------|-------|-------|----------|
| all            | 649    | 3805      | 0.762  | 0.806 | 0.832 | 0.704      |
| person         | 649    | 844       | 0.781  | 0.879 | 0.908 | 0.736    |
| rickshaw       | 649    | 1129      | 0.848  | 0.944 | 0.969 | 0.883    |
| rickshaw van   | 649    | 83        | 0.63   | 0.656 | 0.672 | 0.474    |
| auto rickshaw  | 649    | 228       | 0.878  | 0.908 | 0.957 | 0.885    |
| truck          | 649    | 29        | 0.533  | 0.513 | 0.417 | 0.348    |
| pickup truck   | 649    | 65        | 0.819  | 0.846 | 0.902 | 0.679    |
| private car    | 649    | 543       | 0.84   | 0.932 | 0.959 | 0.879    |
| motorcycle     | 649    | 509       | 0.845  | 0.929 | 0.959 | 0.771    |
| bicycle        | 649    | 121       | 0.802  | 0.868 | 0.902 | 0.731    |
| bus            | 649    | 86        | 0.768  | 0.731 | 0.812 | 0.641    |
| micro bus      | 649    | 105       | 0.892  | 0.886 | 0.929 | 0.867    |
| covered van    | 649    | 24        | 0.614  | 0.542 | 0.61  | 0.535    |
| human hauler   | 649    | 39        | 0.653  | 0.846 | 0.823 | 0.671    |

</details>
