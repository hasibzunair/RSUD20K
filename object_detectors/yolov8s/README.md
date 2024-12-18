## Yolov8s

## 1. Specification of dependencies
```bash
git clone https://github.com/hasibzunair/RSUD20K.git
cd RSUD20K/object_detectors/yolov8s
conda create -n yolo8s python=3.8 -y
conda activate yolo8s
pip install ultralytics
```


## 2. Training and Evaluation

To train YOLOv8s model  run:

```bash
python train.py --yaml_path ./data/rsud20k.yaml --batch_size 12 --epochs 400 --device 0
```
Evaluate model on validation or test set. Model checkpoints are saved in `yolov8s/runs` folder.

```bash
python test.py --weights ./runs/detect/train/weights/best.pt --yaml_path ./data/rsud20k.yaml --batch_size 12 --device 0 
```

For inference, download [yolov8s](https://github.com/hasibzunair/RSUD20K/releases/download/v1/yolov8s.pt) file and keep this file under this folder `runs/detect/train/weights/`.

```bash
python infer.py --weights ./runs/detect/train/weights/best.pt --test_image_path ../datasets/rsud20k/images/test/ --save_dir predictions/
```


## 3. Pre-trained models
We provide pretrained models on GitHub Releases for reproducibility. Download the model from [Here](https://github.com/hasibzunair/RSUD20K/releases/download/v1/yolov8s.pt).


## Acknowledgement

This codebase havily build on [ultralytics](https://github.com/ultralytics/ultralytics).





