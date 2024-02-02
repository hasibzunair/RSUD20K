## Yolov8m

## 1. Specification of dependencies
```bash
git clone https://github.com/hasibzunair/RSUD20K.git
cd RSUD20K/object_detectors/yolov8m
conda create -n yolo8m python=3.8 -y
conda activate yolo8m
pip install ultralytics
```


## 2. Training and Evaluation

To train YOLOv8m model, first download the pretrained model from [here](https://github.com/ultralytics/assets/releases/download/v0.0.0/yolov8m.pt) and put them in `yolov8m/runs/detect/train/weights/` folder. Then run:

```bash
python train.py --yaml_path ./data/rsud20k.yaml --batch_size 12 --epochs 400 --device 0
```
Evaluate model on validation or test set. Model checkpoints are saved in yolov8m/runs folder.

```bash
python test.py --weights ./runs/detect/train/weights/best.pt --yaml_path ./data/rsud20k.yaml --batch_size 12 --device 0 
```

Make predictions on set of images.
```bash
python infer.py --weights ./runs/detect/train/weights/best.pt --test_image_path ../datasets/rsud20k/images/test/ --save_dir predictions/
```


## 3. Pre-trained models
We provide pretrained models on GitHub Releases for reproducibility. Download the model from [Here](https://github.com/hasibzunair/bdss20k-dataset/releases/download/0.0.2/best.pt).

## Acknowledgement

This codebase havily build on [ultralytics](https://github.com/ultralytics/ultralytics).



