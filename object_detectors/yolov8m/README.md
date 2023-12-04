## Yolov8m

## 1. Specification of dependencies
```bash
git clone https://github.com/hasibzunair/bdss20k-dataset.git
cd bdss20k-dataset/object_detectors/yolov8m
conda create -n yolo8m python=3.8 -y
conda activate yolo8m
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

To train YOLOv8m model, first download the pretrained model from [here](https://github.com/hasibzunair/bdss20k-dataset/releases/download/0.0.2/best.pt) and put them in `yolov8m/runs/detect/train/weights/` folder. Then run:

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

#### Validation Results
| Category      | Images | Instances | Box(P) | R    | mAP50 | mAP50-95 |
|---------------|--------|-----------|--------|------|-------|----------|
| all           | 1004   | 7385      | 0.805  | 0.727| 0.812 | 0.664    |
| person        | 1004   | 1917      | 0.862  | 0.817| 0.903 | 0.665    |
| rickshaw      | 1004   | 1587      | 0.873  | 0.849| 0.924 | 0.783    |
| rickshaw van  | 1004   | 240       | 0.774  | 0.692| 0.780 | 0.506    |
| auto rickshaw | 1004   | 590       | 0.897  | 0.887| 0.950 | 0.827    |
| truck         | 1004   | 65        | 0.649  | 0.569| 0.669 | 0.583    |
| pickup truck  | 1004   | 74        | 0.798  | 0.689| 0.790 | 0.617    |
| private car   | 1004   | 1420      | 0.882  | 0.854| 0.921 | 0.786    |
| motorcycle    | 1004   | 860       | 0.870  | 0.842| 0.915 | 0.706    |
| bicycle       | 1004   | 146       | 0.765  | 0.602| 0.722 | 0.544    |
| bus           | 1004   | 182       | 0.796  | 0.730| 0.850 | 0.734    |
| micro bus     | 1004   | 241       | 0.789  | 0.637| 0.767 | 0.698    |
| covered van   | 1004   | 40        | 0.747  | 0.592| 0.638 | 0.555    |
| human hauler  | 1004   | 23        | 0.764  | 0.696| 0.726 | 0.628    |

#### Test Results

| Category       | Images | Instances | Box(P) | R     | mAP50 | mAP50-95 |
|----------------|--------|-----------|--------|-------|-------|----------|
| all            | 649    | 3805      | 0.794  | 0.793 | 0.856 | 0.718    |
| person         | 649    | 844       | 0.792  | 0.850 | 0.905 | 0.717    |
| rickshaw       | 649    | 1129      | 0.855  | 0.920 | 0.965 | 0.873    |
| rickshaw van   | 649    | 83        | 0.641  | 0.753 | 0.761 | 0.538    |
| auto rickshaw  | 649    | 228       | 0.880  | 0.931 | 0.960 | 0.883    |
| truck          | 649    | 29        | 0.581  | 0.483 | 0.490 | 0.407    |
| pickup truck   | 649    | 65        | 0.905  | 0.800 | 0.887 | 0.631    |
| private car    | 649    | 543       | 0.840  | 0.932 | 0.960 | 0.876    |
| motorcycle     | 649    | 509       | 0.860  | 0.898 | 0.955 | 0.769    |
| bicycle        | 649    | 121       | 0.844  | 0.806 | 0.899 | 0.710    |
| bus            | 649    | 86        | 0.584  | 0.636 | 0.740 | 0.606    |
| micro bus      | 649    | 105       | 0.908  | 0.886 | 0.941 | 0.871    |
| covered van    | 649    | 24        | 0.834  | 0.626 | 0.780 | 0.696    |
| human hauler   | 649    | 39        | 0.793  | 0.784 | 0.886 | 0.753    |


## 5. Pre-trained models
We provide pretrained models on GitHub Releases for reproducibility. Download the model from [Here](https://github.com/hasibzunair/bdss20k-dataset/releases/download/0.0.2/best.pt).

## Acknowledgement

This codebase havily build on [ultralytics](https://github.com/ultralytics/ultralytics).


#### Extra
<details>
  <summary>Validation results</summary>

| Category      | Images | Instances | Box(P) | R    | mAP50 | mAP50-95 |
|---------------|--------|-----------|--------|------|-------|----------|
| all           | 1004   | 7385      | 0.805  | 0.727| 0.812 | 0.664    |
| person        | 1004   | 1917      | 0.862  | 0.817| 0.903 | 0.665    |
| rickshaw      | 1004   | 1587      | 0.873  | 0.849| 0.924 | 0.783    |
| rickshaw van  | 1004   | 240       | 0.774  | 0.692| 0.780 | 0.506    |
| auto rickshaw | 1004   | 590       | 0.897  | 0.887| 0.950 | 0.827    |
| truck         | 1004   | 65        | 0.649  | 0.569| 0.669 | 0.583    |
| pickup truck  | 1004   | 74        | 0.798  | 0.689| 0.790 | 0.617    |
| private car   | 1004   | 1420      | 0.882  | 0.854| 0.921 | 0.786    |
| motorcycle    | 1004   | 860       | 0.870  | 0.842| 0.915 | 0.706    |
| bicycle       | 1004   | 146       | 0.765  | 0.602| 0.722 | 0.544    |
| bus           | 1004   | 182       | 0.796  | 0.730| 0.850 | 0.734    |
| micro bus     | 1004   | 241       | 0.789  | 0.637| 0.767 | 0.698    |
| covered van   | 1004   | 40        | 0.747  | 0.592| 0.638 | 0.555    |
| human hauler  | 1004   | 23        | 0.764  | 0.696| 0.726 | 0.628    |

</details>


<details>
  <summary>Test results</summary>

| Category       | Images | Instances | Box(P) | R     | mAP50 | mAP50-95 |
|----------------|--------|-----------|--------|-------|-------|----------|
| all            | 649    | 3805      | 0.794  | 0.793 | 0.856 | 0.718    |
| person         | 649    | 844       | 0.792  | 0.850 | 0.905 | 0.717    |
| rickshaw       | 649    | 1129      | 0.855  | 0.920 | 0.965 | 0.873    |
| rickshaw van   | 649    | 83        | 0.641  | 0.753 | 0.761 | 0.538    |
| auto rickshaw  | 649    | 228       | 0.880  | 0.931 | 0.960 | 0.883    |
| truck          | 649    | 29        | 0.581  | 0.483 | 0.490 | 0.407    |
| pickup truck   | 649    | 65        | 0.905  | 0.800 | 0.887 | 0.631    |
| private car    | 649    | 543       | 0.840  | 0.932 | 0.960 | 0.876    |
| motorcycle     | 649    | 509       | 0.860  | 0.898 | 0.955 | 0.769    |
| bicycle        | 649    | 121       | 0.844  | 0.806 | 0.899 | 0.710    |
| bus            | 649    | 86        | 0.584  | 0.636 | 0.740 | 0.606    |
| micro bus      | 649    | 105       | 0.908  | 0.886 | 0.941 | 0.871    |
| covered van    | 649    | 24        | 0.834  | 0.626 | 0.780 | 0.696    |
| human hauler   | 649    | 39        | 0.793  | 0.784 | 0.886 | 0.753    |

</details>

