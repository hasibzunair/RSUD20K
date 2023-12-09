## RTMDET

## 1. Specification of dependencies
MMYOLO relies on PyTorch, MMCV, MMEngine, and MMDetection. Below are quick steps for installation. Please refer to the [Install Guide](https://github.com/open-mmlab/mmyolo/blob/main/docs/en/get_started/installation.md) for more detailed instructions.

```shell
git clone https://github.com/hasibzunair/bdss20k-dataset.git
cd bdss20k-dataset/object_detectors/rtmdet
conda create -n rtmdet python=3.8 pytorch==1.10.1 torchvision==0.11.2 cudatoolkit=11.3 -c pytorch -y
conda activate rtmdet
# install mmyolo dependencies
pip install openmim
mim install "mmengine>=0.6.0"
mim install "mmcv>=2.0.0rc4,<2.1.0"
mim install "mmdet>=3.0.0,<4.0.0"
# Install albumentations
pip install -r requirements/albu.txt
# Install MMYOLO
mim install -v -e .
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
To train rtmdet model, first download the pretrained model from [here](https://download.openmmlab.com/mmyolo/v0/rtmdet/rtmdet_tiny_syncbn_fast_8xb32-300e_coco/rtmdet_tiny_syncbn_fast_8xb32-300e_coco_20230102_140117-dbb1dc83.pth). Then run:

```bash
python tools/train.py configs/rtmdet/rtmdet_tiny_fast_1xb12-40e_custom_train.py
```

```bash
python tools/test.py configs/rtmdet/rtmdet_tiny_fast_1xb12-40e_custom_test.py work_dirs/rtmdet_tiny_fast_1xb12-40e_custom_train/epoch_1.pth --show-dir show_results --cfg-options test_evaluator.classwise=True
```



## 4. Results

#### Validation Results

| Metric             | IoU        | Area    | maxDets | Value |
|--------------------|------------|---------|---------|-------|
| Average Precision  | 0.50:0.95  | all     | 100     | 0.587 |
| Average Precision  | 0.50       | all     | 100     | 0.761 |
| Average Precision  | 0.75       | all     | 100     | 0.655 |
| Average Precision  | 0.50:0.95  | small   | 100     | 0.117 |
| Average Precision  | 0.50:0.95  | medium  | 100     | 0.385 |
| Average Precision  | 0.50:0.95  | large   | 100     | 0.651 |
| Average Recall     | 0.50:0.95  | all     | 1       | 0.534 |
| Average Recall     | 0.50:0.95  | all     | 10      | 0.744 |
| Average Recall     | 0.50:0.95  | all     | 100     | 0.753 |
| Average Recall     | 0.50:0.95  | small   | 100     | 0.272 |
| Average Recall     | 0.50:0.95  | medium  | 100     | 0.643 |
| Average Recall     | 0.50:0.95  | large   | 100     | 0.794 |

#### Test Result
| Evaluation Metric            | IoU Range   | Area    | maxDets | Value |
|------------------------------|-------------|---------|---------|-------|
| Average Precision (AP)       | 0.50:0.95   | all     | 100     | 0.654 |
| Average Precision (AP)       | 0.50        | all     | 100     | 0.837 |
| Average Precision (AP)       | 0.75        | all     | 100     | 0.742 |
| Average Precision (AP)       | 0.50:0.95   | small   | 100     | 0.018 |
| Average Precision (AP)       | 0.50:0.95   | medium  | 100     | 0.467 |
| Average Precision (AP)       | 0.50:0.95   | large   | 100     | 0.678 |
| Average Recall (AR)          | 0.50:0.95   | all     | 1       | 0.588 |
| Average Recall (AR)          | 0.50:0.95   | all     | 10      | 0.796 |
| Average Recall (AR)          | 0.50:0.95   | all     | 100     | 0.801 |
| Average Recall (AR)          | 0.50:0.95   | small   | 100     | 0.021 |
| Average Recall (AR)          | 0.50:0.95   | medium  | 100     | 0.692 |
| Average Recall (AR)          | 0.50:0.95   | large   | 100     | 0.817 |

#### Test Result per category
| category      | mAP   | mAP_50 | mAP_75 | mAP_s | mAP_m | mAP_l |
|---------------|-------|--------|--------|-------|-------|-------|
| person        | 0.635 | 0.866  | 0.773  | 0.0   | 0.462 | 0.713 |
| rickshaw      | 0.814 | 0.952  | 0.902  | nan   | 0.51  | 0.849 |
| rickshaw van  | 0.498 | 0.756  | 0.596  | nan   | 0.086 | 0.544 |
| auto rickshaw | 0.832 | 0.937  | 0.902  | nan   | 0.504 | 0.87  |
| truck         | 0.365 | 0.47   | 0.435  | nan   | 0.577 | 0.345 |
| pickup truck  | 0.567 | 0.913  | 0.505  | nan   | 0.45  | 0.569 |
| private car   | 0.811 | 0.949  | 0.904  | nan   | 0.71  | 0.832 |
| motorcycle    | 0.689 | 0.934  | 0.835  | 0.053 | 0.584 | 0.734 |
| bicycle       | 0.645 | 0.854  | 0.786  | 0.0   | 0.318 | 0.702 |
| bus           | 0.608 | 0.783  | 0.667  | nan   | nan   | 0.614 |
| micro bus     | 0.81  | 0.91   | 0.91   | nan   | nan   | 0.815 |
| covered van   | 0.62  | 0.748  | 0.738  | nan   | nan   | 0.621 |
| human hauler  | 0.608 | 0.81   | 0.699  | nan   | nan   | 0.608 |


## 5. Pre-trained models
We provide pretrained models on GitHub Releases for reproducibility. Download the model from [Here](https://github.com/hasibzunair/bdss20k-dataset/releases/download/0.0.4/best_coco_bbox_mAP_epoch_363.pth).

## Acknowledgement

This codebase havily build on [mmyolo](https://github.com/open-mmlab/mmyolo/tree/main).


## Extra
<details>
  <summary>Validation Results</summary>

| Metric             | IoU        | Area    | maxDets | Value |
|--------------------|------------|---------|---------|-------|
| Average Precision  | 0.50:0.95  | all     | 100     | 0.587 |
| Average Precision  | 0.50       | all     | 100     | 0.761 |
| Average Precision  | 0.75       | all     | 100     | 0.655 |
| Average Precision  | 0.50:0.95  | small   | 100     | 0.117 |
| Average Precision  | 0.50:0.95  | medium  | 100     | 0.385 |
| Average Precision  | 0.50:0.95  | large   | 100     | 0.651 |
| Average Recall     | 0.50:0.95  | all     | 1       | 0.534 |
| Average Recall     | 0.50:0.95  | all     | 10      | 0.744 |
| Average Recall     | 0.50:0.95  | all     | 100     | 0.753 |
| Average Recall     | 0.50:0.95  | small   | 100     | 0.272 |
| Average Recall     | 0.50:0.95  | medium  | 100     | 0.643 |
| Average Recall     | 0.50:0.95  | large   | 100     | 0.794 |

</details>

```
11/21 15:17:58 - mmengine - INFO - bbox_mAP_copypaste: 0.587 0.761 0.655 0.117 0.385 0.651
11/21 15:17:58 - mmengine - INFO - Epoch(val) [400][502/502]    coco/bbox_mAP: 0.5870  coco/bbox_mAP_50: 0.7610  coco/bbox_mAP_75: 0.6550  coco/bbox_mAP_s: 0.1170  coco/bbox_mAP_m: 0.3850  coco/bbox_mAP_l: 0.6510  data_time: 0.0049  time: 0.0341
```




<details>
  <summary>Test Result</summary>

| Evaluation Metric            | IoU Range   | Area    | maxDets | Value |
|------------------------------|-------------|---------|---------|-------|
| Average Precision (AP)       | 0.50:0.95   | all     | 100     | 0.654 |
| Average Precision (AP)       | 0.50        | all     | 100     | 0.837 |
| Average Precision (AP)       | 0.75        | all     | 100     | 0.742 |
| Average Precision (AP)       | 0.50:0.95   | small   | 100     | 0.018 |
| Average Precision (AP)       | 0.50:0.95   | medium  | 100     | 0.467 |
| Average Precision (AP)       | 0.50:0.95   | large   | 100     | 0.678 |
| Average Recall (AR)          | 0.50:0.95   | all     | 1       | 0.588 |
| Average Recall (AR)          | 0.50:0.95   | all     | 10      | 0.796 |
| Average Recall (AR)          | 0.50:0.95   | all     | 100     | 0.801 |
| Average Recall (AR)          | 0.50:0.95   | small   | 100     | 0.021 |
| Average Recall (AR)          | 0.50:0.95   | medium  | 100     | 0.692 |
| Average Recall (AR)          | 0.50:0.95   | large   | 100     | 0.817 |

</details>


<details>
  <summary>test results per category</summary>

| category      | mAP   | mAP_50 | mAP_75 | mAP_s | mAP_m | mAP_l |
|---------------|-------|--------|--------|-------|-------|-------|
| person        | 0.635 | 0.866  | 0.773  | 0.0   | 0.462 | 0.713 |
| rickshaw      | 0.814 | 0.952  | 0.902  | nan   | 0.51  | 0.849 |
| rickshaw van  | 0.498 | 0.756  | 0.596  | nan   | 0.086 | 0.544 |
| auto rickshaw | 0.832 | 0.937  | 0.902  | nan   | 0.504 | 0.87  |
| truck         | 0.365 | 0.47   | 0.435  | nan   | 0.577 | 0.345 |
| pickup truck  | 0.567 | 0.913  | 0.505  | nan   | 0.45  | 0.569 |
| private car   | 0.811 | 0.949  | 0.904  | nan   | 0.71  | 0.832 |
| motorcycle    | 0.689 | 0.934  | 0.835  | 0.053 | 0.584 | 0.734 |
| bicycle       | 0.645 | 0.854  | 0.786  | 0.0   | 0.318 | 0.702 |
| bus           | 0.608 | 0.783  | 0.667  | nan   | nan   | 0.614 |
| micro bus     | 0.81  | 0.91   | 0.91   | nan   | nan   | 0.815 |
| covered van   | 0.62  | 0.748  | 0.738  | nan   | nan   | 0.621 |
| human hauler  | 0.608 | 0.81   | 0.699  | nan   | nan   | 0.608 |

</details>


```
11/24 22:30:32 - mmengine - INFO - bbox_mAP_copypaste: 0.654 0.837 0.742 0.018 0.467 0.678
11/24 22:30:32 - mmengine - INFO - Epoch(test) [55/55]    coco/person_precision: 0.6350  coco/rickshaw_precision: 0.8140  coco/rickshawvan_precision: 0.4980  coco/autorickshaw_precision: 0.8320  coco/truck_precision: 0.3650  coco/pickuptruck_precision: 0.5670  coco/privatecar_precision: 0.8110  coco/motorcycle_precision: 0.6890  coco/bicycle_precision: 0.6450  coco/bus_precision: 0.6080  coco/microbus_precision: 0.8100  coco/coveredvan_precision: 0.6200  coco/humanhauler_precision: 0.6080  coco/bbox_mAP: 0.6540  coco/bbox_mAP_50: 0.8370  coco/bbox_mAP_75: 0.7420  coco/bbox_mAP_s: 0.0180  coco/bbox_mAP_m: 0.4670  coco/bbox_mAP_l: 0.6780  data_time: 3.3587  time: 3.5143
```