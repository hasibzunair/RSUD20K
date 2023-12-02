<div align="center">
  <img width="100%" src="https://user-images.githubusercontent.com/27466624/222385101-516e551c-49f5-480d-a135-4b24ee6dc308.png"/>
  <div>&nbsp;</div>
  <div align="center">
    <b><font size="5">OpenMMLab website</font></b>
    <sup>
      <a href="https://openmmlab.com">
        <i><font size="4">HOT</font></i>
      </a>
    </sup>
    &nbsp;&nbsp;&nbsp;&nbsp;
    <b><font size="5">OpenMMLab platform</font></b>
    <sup>
      <a href="https://platform.openmmlab.com">
        <i><font size="4">TRY IT OUT</font></i>
      </a>
    </sup>
  </div>
  <div>&nbsp;</div>

[![PyPI](https://img.shields.io/pypi/v/mmyolo)](https://pypi.org/project/mmyolo)
[![docs](https://img.shields.io/badge/docs-latest-blue)](https://mmyolo.readthedocs.io/en/latest/)
[![deploy](https://github.com/open-mmlab/mmyolo/workflows/deploy/badge.svg)](https://github.com/open-mmlab/mmyolo/actions)
[![codecov](https://codecov.io/gh/open-mmlab/mmyolo/branch/main/graph/badge.svg)](https://codecov.io/gh/open-mmlab/mmyolo)
[![license](https://img.shields.io/github/license/open-mmlab/mmyolo.svg)](https://github.com/open-mmlab/mmyolo/blob/main/LICENSE)
[![open issues](https://isitmaintained.com/badge/open/open-mmlab/mmyolo.svg)](https://github.com/open-mmlab/mmyolo/issues)
[![issue resolution](https://isitmaintained.com/badge/resolution/open-mmlab/mmyolo.svg)](https://github.com/open-mmlab/mmyolo/issues)

[📘Documentation](https://mmyolo.readthedocs.io/en/latest/) |
[🛠️Installation](https://mmyolo.readthedocs.io/en/latest/get_started/installation.html) |
[👀Model Zoo](https://mmyolo.readthedocs.io/en/latest/model_zoo.html) |
[🆕Update News](https://mmyolo.readthedocs.io/en/latest/notes/changelog.html) |
[🤔Reporting Issues](https://github.com/open-mmlab/mmyolo/issues/new/choose)

</div>



### https://github.com/open-mmlab/mmyolo/blob/main/docs/en/get_started/15_minutes_object_detection.md


python tools/train.py configs/rtmdet/rtmdet_tiny_fast_1xb12-40e_custom_train.py

python tools/test.py configs/rtmdet/rtmdet_tiny_fast_1xb12-40e_custom_test.py work_dirs/rtmdet_tiny_fast_1xb12-40e_custom_train/epoch_1.pth --show-dir show_results --cfg-options test_evaluator.classwise=True

## 🛠️ Installation [🔝](#-table-of-contents)

MMYOLO relies on PyTorch, MMCV, MMEngine, and MMDetection. Below are quick steps for installation. Please refer to the [Install Guide](docs/en/get_started/installation.md) for more detailed instructions.

```shell
conda create -n mmyolo python=3.8 pytorch==1.10.1 torchvision==0.11.2 cudatoolkit=11.3 -c pytorch -y
conda activate mmyolo
pip install openmim
mim install "mmengine>=0.6.0"
mim install "mmcv>=2.0.0rc4,<2.1.0"
mim install "mmdet>=3.0.0,<4.0.0"
git clone https://github.com/open-mmlab/mmyolo.git
cd mmyolo
# Install albumentations
pip install -r requirements/albu.txt
# Install MMYOLO
mim install -v -e .
```

## 👨‍🏫 Tutorial [🔝](#-table-of-contents)

MMYOLO is based on MMDetection and adopts the same code structure and design approach. To get better use of this, please read [MMDetection Overview](https://mmdetection.readthedocs.io/en/latest/get_started.html) for the first understanding of MMDetection.

The usage of MMYOLO is almost identical to MMDetection and all tutorials are straightforward to use, you can also learn about [MMDetection User Guide and Advanced Guide](https://mmdetection.readthedocs.io/en/3.x/).

For different parts from MMDetection, we have also prepared user guides and advanced guides, please read our [documentation](https://mmyolo.readthedocs.io/zenh_CN/latest/).

<details>
<summary>Get Started</summary>

- [Overview](docs/en/get_started/overview.md)
- [Dependencies](docs/en/get_started/dependencies.md)
- [Installation](docs/en/get_started/installation.md)
- [15 minutes object detection](docs/en/get_started/15_minutes_object_detection.md)
- [15 minutes rotated object detection](docs/en/get_started/15_minutes_rotated_object_detection.md)
- [15 minutes instance segmentation](docs/en/get_started/15_minutes_instance_segmentation.md)
- [Resources summary](docs/en/get_started/article.md)

</details>

<details>
<summary>Recommended Topics</summary>

- [How to contribute code to MMYOLO](docs/en/recommended_topics/contributing.md)
- [Training testing tricks](docs/en/recommended_topics/training_testing_tricks.md)
- [MMYOLO model design](docs/en/recommended_topics/model_design.md)
- [Algorithm principles and implementation](docs/en/recommended_topics/algorithm_descriptions/)
- [Replace the backbone network](docs/en/recommended_topics/replace_backbone.md)
- [MMYOLO model complexity analysis](docs/en/recommended_topics/complexity_analysis.md)
- [Annotation-to-deployment workflow for custom dataset](docs/en/recommended_topics/labeling_to_deployment_tutorials.md)
- [Visualization](docs/en/recommended_topics/visualization.md)
- [Model deployment](docs/en/recommended_topics/deploy/)
- [Troubleshooting steps](docs/en/recommended_topics/troubleshooting_steps.md)
- [MMYOLO application examples](docs/en/recommended_topics/application_examples/)
- [MM series repo essential basics](docs/en/recommended_topics/mm_basics.md)
- [Dataset preparation and description](docs/en/recommended_topics/dataset_preparation.md)

</details>

<details>
<summary>Common Usage</summary>

- [Resume training](docs/en/common_usage/resume_training.md)
- [Enabling and disabling SyncBatchNorm](docs/en/common_usage/syncbn.md)
- [Enabling AMP](docs/en/common_usage/amp_training.md)
- [Multi-scale training and testing](docs/en/common_usage/ms_training_testing.md)
- [TTA Related Notes](docs/en/common_usage/tta.md)
- [Add plugins to the backbone network](docs/en/common_usage/plugins.md)
- [Freeze layers](docs/en/common_usage/freeze_layers.md)
- [Output model predictions](docs/en/common_usage/output_predictions.md)
- [Set random seed](docs/en/common_usage/set_random_seed.md)
- [Module combination](docs/en/common_usage/module_combination.md)
- [Cross-library calls using mim](docs/en/common_usage/mim_usage.md)
- [Apply multiple Necks](docs/en/common_usage/multi_necks.md)
- [Specify specific device training or inference](docs/en/common_usage/specify_device.md)
- [Single and multi-channel application examples](docs/en/common_usage/single_multi_channel_applications.md)

</details>

<details>
<summary>Useful Tools</summary>

- [Browse coco json](docs/en/useful_tools/browse_coco_json.md)
- [Browse dataset](docs/en/useful_tools/browse_dataset.md)
- [Print config](docs/en/useful_tools/print_config.md)
- [Dataset analysis](docs/en/useful_tools/dataset_analysis.md)
- [Optimize anchors](docs/en/useful_tools/optimize_anchors.md)
- [Extract subcoco](docs/en/useful_tools/extract_subcoco.md)
- [Visualization scheduler](docs/en/useful_tools/vis_scheduler.md)
- [Dataset converters](docs/en/useful_tools/dataset_converters.md)
- [Download dataset](docs/en/useful_tools/download_dataset.md)
- [Log analysis](docs/en/useful_tools/log_analysis.md)
- [Model converters](docs/en/useful_tools/model_converters.md)

</details>

<details>
<summary>Basic Tutorials</summary>

- [Learn about configs with YOLOv5](docs/en/tutorials/config.md)
- [Data flow](docs/en/tutorials/data_flow.md)
- [Rotated detection](docs/en/tutorials/rotated_detection.md)
- [Custom Installation](docs/en/tutorials/custom_installation.md)
- [Common Warning Notes](docs/zh_cn/tutorials/warning_notes.md)
- [FAQ](docs/en/tutorials/faq.md)

</details>

<details>
<summary>Advanced Tutorials</summary>

- [MMYOLO cross-library application](docs/en/advanced_guides/cross-library_application.md)

</details>

<details>
<summary>Descriptions</summary>

- [Changelog](docs/en/notes/changelog.md)
- [Compatibility](docs/en/notes/compatibility.md)
- [Conventions](docs/en/notes/conventions.md)
- [Code Style](docs/en/notes/code_style.md)

</details>

<summary><b>Supported Datasets</b></summary>

- [x] COCO Dataset
- [x] VOC Dataset
- [x] CrowdHuman Dataset
- [x] DOTA 1.0 Dataset
</details>


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

**Best Weight**
-  best_coco_bbox_mAP_epoch_363.pth