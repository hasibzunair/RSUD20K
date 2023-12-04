# BDSS20K

This repo is for BDSS20K: A Bangladesh Urban Scenes Understanding Dataset.

## 1. Dataset
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

Open a new folder named `datasets` and keep it under `object_detectors/` folder. Our project utilizes two prominent data formats: COCO and YOLO. The YOLO format is specifically employed for the Yolov8 variants (l, s, m), while the COCO format is adopted for the rtmdet and detr models. For an in-depth understanding of these formats, explore the COCO format [here](https://roboflow.com/formats/coco-json) and the YOLO format [here](https://roboflow.com/formats/yolov8-pytorch-txt). For details on format, see [here](https://github.com/meituan/YOLOv6/blob/main/docs/Train_custom_data.md#1-prepare-your-own-dataset).

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

To train the different models follow this:

- [Yolov8Small](https://github.com/hasibzunair/bdss20k-dataset/tree/models/object_detectors/yolov8s)
- [Yolov8Medium](https://github.com/hasibzunair/bdss20k-dataset/tree/models/object_detectors/yolov8m)
- [Yolov8Large](https://github.com/hasibzunair/bdss20k-dataset/tree/models/object_detectors/yolov8l)
- [RTMDET](https://github.com/hasibzunair/bdss20k-dataset/tree/models/object_detectors/rtmdet)
- [DETR](https://github.com/hasibzunair/bdss20k-dataset/tree/models/object_detectors/detr)

##  3. Pre-trained models(Will Update)

| Model          | Params(M)	      | mAP(%) | Download    |
|------------------|------------------|---------|-------------|
| yolov8s        | 4.8  | 76.06   | [Download](#) |
| yolov8m | 4.8  | 84.02   | [Download](#) |
| YOLOV8l           | 4.8          | 39.31   | [Download](#) |
| rtmdet           | 4.8          | 39.31   | [Download](#) |
| dete           | 4.8          | 39.31   | [Download](#) |

### Acknowledgements

This codebase is built on top of:

- [Ultralytics](https://github.com/ultralytics/ultralytics)
- [MMDetection](https://github.com/open-mmlab/mmdetection)
- [MMYolo](https://github.com/open-mmlab/mmyolo)
