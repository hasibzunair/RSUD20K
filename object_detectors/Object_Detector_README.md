# BDSS20K

This repo is for BDSS20K: A Bangladesh Urban Scenes Understanding Dataset.

## 1. Dataset

videos: has sub folders of different places/conditions which itself has clips of different streets.

v1: train/val/test has 54//19/11 videos group partitioned in street level from `videos`.

v2: train/val/test has frames from `v1`. 18762, 1008, 656 images.

v3: 3,985 training images and labels, 14,762 unlabeled images. Some images dropped as no target objects.

v4: 3,985 training images and labels, 126 validation images and labels from the train set itself.

`bdss5k` : train, val and test sets have 3,985, 1,004 and 649 image/label pairs respectively. `train` split was used to train YOLOv6-M6 model for pseudo labeleing. `val` and `test` splits were created by semi-automatic labeleing.

For details on format, see [here](https://github.com/meituan/YOLOv6/blob/main/docs/Train_custom_data.md#1-prepare-your-own-dataset). The class list for this task is:

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

Open a new folder named `datasets` and keep it there. Our project utilizes two prominent data formats: COCO and YOLO. The YOLO format is specifically employed for the Yolov8 variants (l, s, m), while the COCO format is adopted for the rtmdet and detr models. For an in-depth understanding of these formats, explore the COCO format [here](https://roboflow.com/formats/coco-json) and the YOLO format [here](https://roboflow.com/formats/yolov8-pytorch-txt).

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

To train the models follow this:

- [Yolov8Large](<>)
- [Yolov8Medium](<>)
- [Yolov8Small](<>)
- [RTMDET](<>)
- [DETR](<>)

### Done

- [x] yolov8l
- [ ] yolov8m
- [ ] yolov8s
- [ ] rtmdet
- [ ] detr

### Acknowledgements

This codebase is built on top of:

- Ultralytics: https://github.com/ultralytics/ultralytics
- MMDetection: https://github.com/open-mmlab/mmdetection
- MMYolo: https://github.com/open-mmlab/mmyolo
