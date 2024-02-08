# RSUD20K

This repo is for RSUD20K: A Bangladesh Urban Scenes Understanding Dataset.

## 1. Folder Structure
To reproduce the result, make sure you have this folder structure.
```bash
object_detectors
├── datasets
│   ├── rsud20k
│   │   ├── images
│   │   └── labels
├── datasets_json
│   ├── annotations
|   │   └── test_rsud20k.json
|   │   └── train_rsud20k.json
|   │   └── val_rsud20k.json
│   ├── test_rsud20k
│   ├── train_rsud20k
│   ├── val_rsud20k
├── detr
├── rtmdet
├── yolov8s
│   └── data
│       └── rsud20k.yml
├── yolov8m
│   └── data
│       └── rsud20k.yml
└── yolov8l
    └── data
        └── rsud20k.yml
```
## 1. Dataset

Open a new folder named `datasets` and keep it under `object_detectors/` folder. Our project utilizes two prominent data formats: **COCO** and **YOLO**. The YOLO format is specifically employed for the Yolov8 variants (l, s, m), while the COCO format is adopted for the rtmdet and detr models. For an in-depth understanding of these formats, explore the COCO format [here](https://roboflow.com/formats/coco-json) and the YOLO format [here](https://roboflow.com/formats/yolov8-pytorch-txt). For details on format, see [here](https://github.com/meituan/YOLOv6/blob/main/docs/Train_custom_data.md#1-prepare-your-own-dataset).

**Example of data formats**:

```bash
# coco format
dataset
├── annotations
│   ├── train.json
│   ├── val.json
│   ├── test.json
├── train
│   ├── 0000000001.jpg
│   ├── 0000000002.jpg
│   ├── 0000000003.jpg
├── val
│   ├── 0000000001.jpg
│   ├── 0000000002.jpg
│   ├── 0000000003.jpg
├── test
│   ├── 0000000001.jpg
│   ├── 0000000002.jpg
│   ├── 0000000003.jpg
```

```bash
# yolo format
dataset
├── images
│   ├── train
│   │   ├── 0000000001.jpg
│   │   ├── 0000000002.jpg
│   │   ├── 0000000003.jpg
│   ├── val
│   │   ├── 0000000001.jpg
│   │   ├── 0000000002.jpg
│   │   ├── 0000000003.jpg
│   ├── test
│   │   ├── 0000000001.jpg
│   │   ├── 0000000002.jpg
│   │   ├── 0000000003.jpg
├── labels
│   ├── train
│   │   ├── 0000000001.txt
│   │   ├── 0000000002.txt
│   │   ├── 0000000003.txt
│   ├── val
│   │   ├── 0000000001.txt
│   │   ├── 0000000002.txt
│   │   ├── 0000000003.txt
│   ├── test
│   │   ├── 0000000001.txt
│   │   ├── 0000000002.txt
│   │   ├── 0000000003.txt
```

## 2. Training and Evaluation

To train different models follow this:

- [Yolov8Small](https://github.com/hasibzunair/bdss20k-dataset/tree/models/object_detectors/yolov8s)
- [Yolov8Medium](https://github.com/hasibzunair/bdss20k-dataset/tree/models/object_detectors/yolov8m)
- [Yolov8Large](https://github.com/hasibzunair/bdss20k-dataset/tree/models/object_detectors/yolov8l)
- [RTMDET](https://github.com/hasibzunair/bdss20k-dataset/tree/models/object_detectors/rtmdet)
- [DETR](https://github.com/hasibzunair/bdss20k-dataset/tree/models/object_detectors/detr)

##  3. Pre-trained models

| Model          | Params(M)	      | mAP(%) | Download    |
|------------------|------------------|---------|-------------|
| `yolov8s`        | 11.2 | 69.4   | [Download](https://github.com/hasibzunair/bdss20k-dataset/releases/download/0.0.1/best.pt) |
| `yolov8m` | 25.9  | 71.8  | [Download](https://github.com/hasibzunair/bdss20k-dataset/releases/download/0.0.2/best.pt) |
| `yolov8l`           | 43.7          | 70.4   | [Download](https://github.com/hasibzunair/bdss20k-dataset/releases/download/0.0.3/best.pt) |
| `rtmdet`           | 4.8          | 65.4   | [Download](https://github.com/hasibzunair/bdss20k-dataset/releases/download/0.0.4/best_coco_bbox_mAP_epoch_363.pth) |
| `detr`           | 41.3          | 49.9   | [Download](https://github.com/hasibzunair/bdss20k-dataset/releases/download/0.0.5/epoch_400.pth) |


### Acknowledgements

This codebase is built on top of:

- [Ultralytics](https://github.com/ultralytics/ultralytics)
- [MMDetection](https://github.com/open-mmlab/mmdetection)
- [MMYolo](https://github.com/open-mmlab/mmyolo)
