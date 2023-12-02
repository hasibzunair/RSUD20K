# YoloV8L

To train yolov8l, we have used [ultralytics](https://github.com/ultralytics/ultralytics)


## 1. Specification of dependencies
This code requires Python>=3.8 environment with PyTorch>=1.8 and  CUDA 11.4. Create and activate the following conda envrionment.

```bash
conda create -n yolov8l python=3.8 -y
conda activate yolov8l

# Install ultralytics
pip install ultralytics

# Clone this repo
git clone https://github.com/hasibzunair/bdss20k-dataset.git
cd models/yolov8l
```

## 2. Dataset
Open a new folder named datasets and keep it there in YOLO format.

**Dataset statistics**:

| Name  | Number of images/label pairs |
| ------------- | ------------- |
| `train`  | 3,985 |
| `val`  | 1004 |
| `test`  | 649 |
| `pseudo`  | 14,762 |

## 2. Training and Evaluation

```
# To train a YOLOv8l model
python train.py --yaml_path './data/bdss20k.yaml' --batch_size 12 --epoch 400 --device 0

# To test a YOLOv8l model
python test.py --weights 'runs/detect/train/weights/best.pt' --yaml_path './data/bdss20k.yaml' --test_image_path '../datasets/bdss20k/images/test/' --save_dir 'predictions/'
```















https://github.com/ultralytics/ultralytics/issues/3920
https://docs.ultralytics.com/modes/val/#arguments

Run special commands to see version, view settings, run checks and more:
```
        yolo help
        yolo checks
        yolo version
        yolo settings
        yolo copy-cfg
        yolo cfg       
```
https://github.com/ultralytics/ultralytics/blob/b6baae584c3cf8560300a8eb1c267f68e63554bb/docs/en/quickstart.md?plain=1#L189
https://github.com/ultralytics/ultralytics/blob/b6baae584c3cf8560300a8eb1c267f68e63554bb/docs/en/quickstart.md?plain=1#L189

Settings 
/home/shakib/.config/Ultralytics/settings.yaml

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

##### Acknowledgement
- [ultralytics]()