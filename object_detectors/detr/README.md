## DETR

## 1. Specification of dependencies
MMDetection works on Linux, Windows, and macOS. It requires Python 3.7+, CUDA 9.2+, and PyTorch 1.8+. Please refer to the [Install Guide](https://mmdetection.readthedocs.io/en/latest/get_started.html) for more detailed instructions.

```shell
git clone https://github.com/hasibzunair/bdss20k-dataset.git
cd bdss20k-dataset/object_detectors/detr
conda create -n detr python=3.8 pytorch==1.10.1 torchvision==0.11.2 cudatoolkit=11.3 -c pytorch -y
conda activate detr
# install dependencies
pip install -U openmim
mim install "mmengine>=0.7.0"
mim install "mmcv>=2.0.0rc4"
# Install mmdetection
%pip install -e .
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
| `pseudo` | 14,696                       |

Open a new folder named `datasets` and keep it under `object_detectors/` folder. Our project utilizes two prominent data formats: COCO and YOLO. The YOLO format is specifically employed for the Yolov8 variants (l, s, m), while the COCO format is adopted for the rtmdet and detr models. For an in-depth understanding of these formats, explore the COCO format [here](https://roboflow.com/formats/coco-json) and the YOLO format [here](https://roboflow.com/formats/yolov8-pytorch-txt). 


## 3. Training and Evaluation
To train rtmdet model, first download the pretrained model from [here](https://download.openmmlab.com/mmyolo/v0/rtmdet/rtmdet_tiny_syncbn_fast_8xb32-300e_coco/rtmdet_tiny_syncbn_fast_8xb32-300e_coco_20230102_140117-dbb1dc83.pth). Then run:

```bash
python tools/train.py configs/detr/detr_r50_8xb2-150e_custom_train.py
```

```bash
python tools/test.py configs/detr/detr_r50_8xb2-400e_custom_test.py work_dirs/detr_r50_8xb2-400e_custom_train/epoch_400.pth --show-dir show_results --cfg-options test_evaluator.classwise=True`
```

## 4. Results


##### Validation

| Metric                    | IoU         | Area    | MaxDets | Value |
|---------------------------|-------------|---------|---------|-------|
| Average Precision (AP)    | 0.50:0.95   | all     | 100     | 0.504 |
| Average Precision (AP)    | 0.50        | all     | 1000    | 0.659 |
| Average Precision (AP)    | 0.75        | all     | 1000    | 0.566 |
| Average Precision (AP)    | 0.50:0.95   | small   | 1000    | 0.106 |
| Average Precision (AP)    | 0.50:0.95   | medium  | 1000    | 0.280 |
| Average Precision (AP)    | 0.50:0.95   | large   | 1000    | 0.567 |
| Average Recall (AR)       | 0.50:0.95   | all     | 100     | 0.575 |
| Average Recall (AR)       | 0.50:0.95   | all     | 300     | 0.575 |
| Average Recall (AR)       | 0.50:0.95   | all     | 1000    | 0.575 |
| Average Recall (AR)       | 0.50:0.95   | small   | 1000    | 0.136 |
| Average Recall (AR)       | 0.50:0.95   | medium  | 1000    | 0.377 |
| Average Recall (AR)       | 0.50:0.95   | large   | 1000    | 0.630 |


##### Testing
| Metric                    | IoU         | Area    | MaxDets | Value |
|---------------------------|-------------|---------|---------|-------|
| Average Precision (AP)    | 0.50:0.95   | all     | 100     | 0.499 |
| Average Precision (AP)    | 0.50        | all     | 1000    | 0.639 |
| Average Precision (AP)    | 0.75        | all     | 1000    | 0.564 |
| Average Precision (AP)    | 0.50:0.95   | small   | 1000    | 0.110 |
| Average Precision (AP)    | 0.50:0.95   | medium  | 1000    | 0.373 |
| Average Precision (AP)    | 0.50:0.95   | large   | 1000    | 0.514 |
| Average Recall (AR)       | 0.50:0.95   | all     | 100     | 0.570 |
| Average Recall (AR)       | 0.50:0.95   | all     | 300     | 0.570 |
| Average Recall (AR)       | 0.50:0.95   | all     | 1000    | 0.570 |
| Average Recall (AR)       | 0.50:0.95   | small   | 1000    | 0.138 |
| Average Recall (AR)       | 0.50:0.95   | medium  | 1000    | 0.457 |
| Average Recall (AR)       | 0.50:0.95   | large   | 1000    | 0.587 |

#### Test Result per category
| category     | mAP   | mAP_50 | mAP_75 | mAP_s | mAP_m | mAP_l |
|--------------|-------|--------|--------|-------|-------|-------|
| person       | 0.592 | 0.816  | 0.721  | 0.05  | 0.411 | 0.671 |
| rickshaw     | 0.784 | 0.911  | 0.869  | nan   | 0.489 | 0.816 |
| rickshawvan  | 0.334 | 0.527  | 0.354  | nan   | 0.092 | 0.374 |
| autorickshaw | 0.802 | 0.904  | 0.881  | nan   | 0.592 | 0.828 |
| truck        | 0.077 | 0.118  | 0.093  | nan   | 0.191 | 0.043 |
| pickuptruck  | 0.136 | 0.183  | 0.145  | nan   | 0.0   | 0.139 |
| privatecar   | 0.778 | 0.92   | 0.873  | nan   | 0.676 | 0.799 |
| motorcycle   | 0.671 | 0.897  | 0.808  | 0.278 | 0.553 | 0.713 |
| bicycle      | 0.561 | 0.751  | 0.701  | 0.0   | 0.356 | 0.593 |
| bus          | 0.415 | 0.661  | 0.41   | nan   | nan   | 0.417 |
| microbus     | 0.488 | 0.545  | 0.545  | nan   | nan   | 0.489 |
| coveredvan   | 0.219 | 0.289  | 0.277  | nan   | nan   | 0.226 |
| humanhauler  | 0.57  | 0.784  | 0.655  | nan   | nan   | 0.57  |

## 5. Pre-trained models
We provide pretrained models on GitHub Releases for reproducibility. Download the model from [Here](https://github.com/hasibzunair/bdss20k-dataset/releases/download/0.0.5/epoch_400.pth).

## Acknowledgement
This codebase havily build on [mmdetection](https://github.com/open-mmlab/mmdetection/tree/main).
