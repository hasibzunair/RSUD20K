## DETR

## 1. Specification of dependencies
MMDetection works on Linux, Windows, and macOS. It requires Python 3.7+, CUDA 9.2+, and PyTorch 1.8+. Please refer to the [Install Guide](https://mmdetection.readthedocs.io/en/latest/get_started.html) for more detailed instructions.

```shell
git clone https://github.com/hasibzunair/RSUD20Kgit
cd RSUD20K/object_detectors/detr
conda create -n detr python=3.8 pytorch==1.10.1 torchvision==0.11.2 cudatoolkit=11.3 -c pytorch -y
conda activate detr
# install dependencies
pip install -U openmim
mim install "mmengine>=0.7.0"
mim install "mmcv>=2.0.0rc4"
# Install mmdetection
%pip install -e .
```

## 2. Training and Evaluation
To train rtmdet model, first download the pretrained model from [here](https://download.openmmlab.com/mmyolo/v0/rtmdet/rtmdet_tiny_syncbn_fast_8xb32-300e_coco/rtmdet_tiny_syncbn_fast_8xb32-300e_coco_20230102_140117-dbb1dc83.pth). Then run:

```bash
python tools/train.py configs/detr/detr_r50_8xb2-150e_custom_train.py
```

```bash
python tools/test.py configs/detr/detr_r50_8xb2-400e_custom_test.py work_dirs/detr_r50_8xb2-400e_custom_train/epoch_400.pth --show-dir show_results --cfg-options test_evaluator.classwise=True`
```

## 3. Pre-trained models
We provide pretrained models on GitHub Releases for reproducibility. Download the model from [Here](https://github.com/hasibzunair/bdss20k-dataset/releases/download/0.0.5/epoch_400.pth).

## Acknowledgement
This codebase havily build on [mmdetection](https://github.com/open-mmlab/mmdetection/tree/main).
