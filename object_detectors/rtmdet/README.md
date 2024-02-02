## RTMDET

## 1. Specification of dependencies
MMYOLO relies on PyTorch, MMCV, MMEngine, and MMDetection. Below are quick steps for installation. Please refer to the [Install Guide](https://github.com/open-mmlab/mmyolo/blob/main/docs/en/get_started/installation.md) for more detailed instructions.

```shell
git clone https://github.com/hasibzunair/RSUD20K.git
cd RSUD20K/object_detectors/rtmdet
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

## 2. Training and Evaluation
To train rtmdet model, first download the pretrained model from [here](https://download.openmmlab.com/mmyolo/v0/rtmdet/rtmdet_tiny_syncbn_fast_8xb32-300e_coco/rtmdet_tiny_syncbn_fast_8xb32-300e_coco_20230102_140117-dbb1dc83.pth). Then run:

```bash
python tools/train.py configs/rtmdet/rtmdet_tiny_fast_1xb12-40e_custom_train.py
```

```bash
python tools/test.py configs/rtmdet/rtmdet_tiny_fast_1xb12-40e_custom_test.py work_dirs/rtmdet_tiny_fast_1xb12-40e_custom_train/epoch_1.pth --show-dir show_results --cfg-options test_evaluator.classwise=True
```


## 3. Pre-trained models
We provide pretrained models on GitHub Releases for reproducibility. Download the model from [Here](https://github.com/hasibzunair/bdss20k-dataset/releases/download/0.0.4/best_coco_bbox_mAP_epoch_363.pth).

## Acknowledgement

This codebase havily build on [mmyolo](https://github.com/open-mmlab/mmyolo/tree/main).

