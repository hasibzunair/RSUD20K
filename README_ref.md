## Tarmak Play Computer Vision

This repo is for Tarmak Play Computer Vision project. Currently the repo hosts training code and models for rim, basketball and person detection as well as the logic for counting baskets and attempts.

![attention](./media/demo.png)

## 1. Specification of dependencies 

This code requires Python 3.8 and CUDA 11.6 (to train models), inference of object detector and logic for counting baskets runs on a mac. Go to your terminal, create and activate the following conda envrionment.

```bash
git clone https://github.com/dktunited/tarmakplay-vision
cd tarmakplay-vision
# Create a fresh environment
conda create -n tarmak python=3.8
pip install moviepy
pip install opencv-python
cd src
pip install -r requirements.txt # for YOLOv6
# Export
conda env export > environment.yml
cd .. 

# or create from environment.yml
conda update conda
conda env create -f environment.yml
conda activate tarmak
```

## 2. Dataset

We built a dataset of rim, basketball and person images and bounding box labels using [labelImg](https://github.com/HumanSignal/labelImg#installation). Images are 1280 × 720 resolution. Data is labeled in YOLO format. For details on format, see [here](https://github.com/meituan/YOLOv6/blob/main/docs/Train_custom_data.md#1-prepare-your-own-dataset). Dataset can be found in GCS in `ai-canada-datasets/data/tarmak_datasets`. The class list for this task is:

```bash
rim
basketball
person
```

**Version of datasets and information**
| Name  | Number of images |
| ------------- | ------------- |
| `tarmak_basketball_datasetv1.zip`  | 3700 |
| `tarmak_basketball_datasetv0.zip`  | 800 |

Open a new folder named `datasets` and keep it there.

## 3. Train and Eval

Train model to detect rim, basketball and person. After training is done, model weights will be saved in `src/runs` folder. Download the pretrained models (S and L operating at 320*320) from [here](https://github.com/meituan/YOLOv6/tree/4364f29bf3244f2e73d0c42a103cd7a9cbb16ca9#mobile-benchmark) and put them in weights folder. Then run: 

```bash
cd src
# S
python tools/train.py --batch 32 --conf configs/yolov6_lite/yolov6_lite_s_finetune.py --data data/basketball.yaml --device 0
# L
python tools/train.py --batch 32 --conf configs/yolov6_lite/yolov6_lite_l_finetune.py --data data/basketball.yaml --device 0
```

Evaluate model on validation or test set. See `src/runs` folder for results.
```bash
python tools/eval.py --data data/basketball.yaml  --weights runs/train/exp/weights/best_ckpt.pt --task val --device 0
```

Make predictions on images or videos.
```bash
# infer on images
python tools/infer.py --weights runs/train/exp/weights/best_ckpt.pt --yaml data/basketball.yaml --source ../datasets/tarmak_basketball_datasetv1/images/val  --device 0
# infer on videos
python tools/infer.py --weights runs/train/exp/weights/best_ckpt.pt --yaml data/basketball.yaml --source ../datasets/resized_videos/ --device 0
```

If you are satisfied with the model, you can convert it into ONNX format using: 
```bash
python deploy/ONNX/export_onnx.py --weights runs/train/exp/weights/best_ckpt.pt --end2end --simplify --topk-all 100 --iou-thres 0.65 --conf-thres 0.35 --img-size 320 320 --dynamic-batch --ort
```

To further convert the model into ORT format, make a new folder and keep your *.onnx model there, then run:
```bash
pip install onnxruntime
python -m onnxruntime.tools.convert_onnx_models_to_ort YOUR_PATH_TO_FOLDER_WITH_ONNX_MODEL
```
In the new directory you will have the `.ort` file along with the config files.

## 4. Rim, person and basketball detector

See [object_detector](./object_detector) folder for details on how to use the model in ONNX or ORT format.

## 5. Count baskets

See [count_baskets](./count_baskets) folder for details on how to use the object detection model in combination with ball trajectory prediction with count baskets and attempts.

## 6. Player position

TBA. See [tba](./tba).

## Project Notes

<details><summary>Click to view</summary>
<br>

**[Sept 13, 2023]** Counts baskets!

**[Aug 16, 2023]** V1 models of YOLOv6Lite S and L done. See [here](https://github.com/dktunited/tarmakplay-vision/releases/tag/v1).

**[Aug 8, 2023]** Dataset version 1 done. Roughly 3.7K images and box labels of rim, basketball and person.


**[Aug 2, 2023]** Save labels from images

```bash
python tools/infer.py --weights runs/yolov6lite_s_600imgs_first/train/exp/weights/best_ckpt.pt --yaml data/basketball.yaml --source ../datasets/chunk-1827-2826 --device 0 --save-txt
```

**[Aug 1, 2023]** To train a model, clone YOLOv6 source code from this commit: https://github.com/meituan/YOLOv6/tree/4364f29bf3244f2e73d0c42a103cd7a9cbb16ca9

```bash
pip install -r requirements.txt
cd src
# train
python tools/train.py --batch 32 --conf configs/yolov6_lite/yolov6_lite_s_finetune.py --data data/basketball.yaml --device 0
# eval
python tools/eval.py --data data/basketball.yaml  --weights runs/train/exp/weights/best_ckpt.pt --task val --device 0
# infer on images
python tools/infer.py --weights runs/train/exp/weights/best_ckpt.pt --yaml data/basketball.yaml --source ../datasets/basketball_datasetv0/images/val  --device 0
# infer on videos
python tools/infer.py --weights runs/train/exp/weights/best_ckpt.pt --yaml data/basketball.yaml --source ../datasets/resized_videos/Outdoor-FrontMin.mp4 --device 0
# infer on images and save .txt files for pseudo labels
python tools/infer.py --weights runs/train/exp/weights/best_ckpt.pt --yaml data/basketball.yaml --source ../datasets/chunk/images/  --device 0 --save-txt
```

**[July 11, 2023]** Convert YOLOv6 PyTorch model to ONNX:
```bash
%cd ..
%cd src
!python deploy/ONNX/export_onnx.py --weights ./weights/yolov6lite_s_tarmakv0.pt --end2end --simplify --topk-all 100 --iou-thres 0.65 --conf-thres 0.35 --img-size 320 320 --dynamic-batch --ort
```

Using YOLOv6 source code from this commit: https://github.com/meituan/YOLOv6/tree/4364f29bf3244f2e73d0c42a103cd7a9cbb16ca9

**[July 3, 2023]** To run labelImg on M1:
```bash
# if clone does not work, download zip and put folder in datasets
git clone https://github.com/heartexlabs/labelImg/tree/pyside6
pip install lxml
pip install Pyside6
brew install pyside6
make pyside6
# run app
cd datasets/labelImg
python labelImg.py ../frames/ ../predef_cls.txt
```


**[June 28, 2023]** To preprocess video files, run:

```bash
# resize videos
python utils/resize_and_save_videos.py --source ./datasets/videos/ --dest ./datasets/resized_videos
# videos to frames
python utils/videos_to_frames.py --source ./datasets/resized_videos/ --dest ./datasets/frames --maxframes 1000
```

To label data

```bash
pip install labelImg
labelImg datasets/frames/ datasets/predef_cls.txt
```

**[June 26, 2023]** Resize videos to 1280 × 720 resolution from the initial 4K ones.

</details>

## Acknowledgements
This codebase is built on top of https://github.com/meituan/YOLOv6. 