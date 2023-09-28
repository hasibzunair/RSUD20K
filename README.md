## BDSS20K

This repo is for BDSS20K: A Bangladesh Urban Scenes Understanding Dataset.

## 1. Specification of dependencies

This code requires Python 3.8 and CUDA 11.4. Create and activate the following conda envrionment.

```bash
git clone https://github.com/dktunited/tarmakplay-vision
cd tarmakplay-vision
# Create fresh env
conda create -n bdstr python=3.8
pip install moviepy
pip install opencv-python
pip install -r src/requirements.txt # for YOLOv6
# Export
conda env export > environment.yml

# OR create from environment.yml
conda update conda
conda env create -f environment.yml
conda activate bdstr
```

## 2. Dataset

videos: has sub folders of different places/conditions which itself has clips of different streets.

v1: train/val/test has 54//19/11 videos group partitioned in street level from `videos`.

v2: train/val/test has frames from `v1`. 18762, 1008, 656 images.

v3: 3,985 training images and labels, 14,792 unlabeled images. Some images dropped as no target objects.

`bdss_4k`: 3,985 training images and labels, 126 validation images and labels from the train set itself.

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

**Version of datasets and information**:

| Name  | Number of images |
| ------------- | ------------- |
| `TBA.zip`  | TBA |

Open a new folder named `datasets` and keep it there.

## 3. Training and Evaluation

To train a YOLOv6 model, first download the pretrained model (S and L operating at 320*320) from [here](https://github.com/meituan/YOLOv6/tree/4364f29bf3244f2e73d0c42a103cd7a9cbb16ca9#mobile-benchmark) and put them in `src/weights` folder. Then run:

```bash
cd src
# Lite-S
python tools/train.py --batch 32 --conf configs/yolov6_lite/yolov6_lite_s_finetune.py --data data/bdstreets.yaml --device 0
# L
python tools/train.py --batch 32 --conf configs/yolov6l_finetune.py --data data/bdstreets.yaml --device 0
# M6
python tools/train.py --batch 12 --conf configs/yolov6m6_finetune.py --data data/bdstreets.yaml --device 0
```

Initial Results:

**YOLOv6-Lite-S**: Epoch: 399 | mAP@0.5: 0.7726942928598644 | mAP@0.50:0.95: 0.48885455925036714.
**YOLOv6 M6**: Epoch: 399 | mAP@0.5: 0.9927252534165519 | mAP@0.50:0.95: 0.7764636844596305

Evaluate model on validation or test set. Model checkpoints are saved in `src/runs` folder.

```bash
python tools/eval.py --data data/bdstreets.yaml  --weights runs/train/exp/weights/best_ckpt.pt --task val --device 0
```

Make predictions on set of images or videos.

```bash
# infer on images
python tools/infer.py --weights runs/train/exp/weights/best_ckpt.pt --yaml data/bdstreets.yaml --source ../datasets/bdss_4k/images/val  --device 0
# infer on videos
python tools/infer.py --weights runs/train/exp/weights/best_ckpt.pt --yaml data/bdstreets.yaml --source ../datasets/resized_videos/ --device 0
# infer on images and save .txt files for pseudo labels
python tools/infer.py --weights runs/train/exp/weights/best_ckpt.pt --yaml data/bdstreets.yaml --source ../datasets/images/  --device 0 --save-txt
```

To convert it into ONNX format, do:

```bash
python deploy/ONNX/export_onnx.py --weights runs/train/exp/weights/best_ckpt.pt --end2end --simplify --topk-all 100 --iou-thres 0.65 --conf-thres 0.35 --img-size 320 320 --dynamic-batch --ort
```

## Project Notes

<details><summary>Click to view</summary>
<br>

**[Sept 28, 2023]** For semi-automatic stage, val and test set images are inferred using YOLOv6 M6.

**[Sept 22, 2023]** 3,985 training images and labels, 14,792 unlabeled images.  1008 val, and 656 test. Total of 20,441 images. To train a YOLOv6 model, clone YOLOv6 source code from this commit: https://github.com/meituan/YOLOv6/tree/4364f29bf3244f2e73d0c42a103cd7a9cbb16ca9.

**[Sept 14, 2023]** As there are typically no lanes and roads are thin, viewpoints are a problem for an object (i.e. front and back side of object in train14861.jpg, train17305.jpg same object but front back viewpoints, also small, so very hard cases) as it is coming and going in the road so need to recognize both viewpoints correctly. This is not usual in other scene datasets. Also, most vehicles are human ridden (rickshaw, rickshaw van, motorcycle, bicycle) so difficult to recognize with person on it. Truck, pickup truck covered van similar, require fine grained understanding, especially when objects are far or close since big or small sizes.

**[Aug 4, 2023]** Initial data labeling stats (1hr 74 images).

LabelImg tool on macos:

```bash
git clone https://github.com/HumanSignal/labelImg
cd labelImg
pip3 install pyqt5 lxml
make qt5py3
python3 labelImg.py ../../datasets/bdss_v3/chunk2/ ../../datasets/bdss_v3/chunk2_labels/classes.txt
```

**[Aug 3, 2023]** Train images split into labeled (4000) and unlabeled (14,762) sets.

Total images are 23,246 which has 18,762 train, 1008 val, and 656 test.

Labeleing criteria:

* `person` : draw boxes on persons only that are walking, not on vehicles.
* `rickshaw` : boxes without person if possible. should be a tight box around the object. 
* `rickshaw van` : boxes around any three wheeler vans pulled by humans (e.g. selling vegetables or fruits).
* `auto rickshaw` : any CNG, three wheeler electric veheicles
* `truck`: big or small trucks
* `pickup truck` : blue small vans, other small vans.
* `private car` : any private car (includes jeeps too).
* `motorcycle` : box should not have person if possible.
* `bicycle` : box should not have person if possible.
* `bus`: any bus, small or big (e.g ena bus).
* `micro bus`: big cars like ambulance or other 7/8 seater cars (also Noah).
* `covered van`: like pickup, but covered.
* `human hauler`: leguna!

In general, all boxes should be tight as possible. If the object is occluded more than 50%, don't label. If more than 50% is visible, only then draw tight box around it. In case of very dense scenes, a bit of overlapping boxes are fine.

**[Aug 3, 2023]** List of classes:

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

**[July 19, 2023]** Inspect data with labeImg
```
labelImg [IMAGE_PATH] [PRE-DEFINED CLASS FILE]
```

**[July 14, 2023]** Get frames from videos. For val and test, frame sampling rate is 60,60 and for train it is 400.

```
python utils/videos_to_frames.py --source ./datasets/bdss_v1/test --dest ./datasets/bdss_v2/test --maxframes 60
python utils/videos_to_frames.py --source ./datasets/bdss_v1/val --dest ./datasets/bdss_v2/val --maxframes 60
python utils/videos_to_frames.py --source ./datasets/bdss_v1/train --dest ./datasets/bdss_v2/train --maxframes 400
```

**[July 6, 2023]** Started project!

The videos were in format:

```videos/
        mawa/
            *.MOV
            ...
        dhanmondi/
            *.MOV
            ...
        night/
            *.MOV
            ...
        rainydays/
            *.MOV
            ...
```

Where each folder has video clips of different streets of the same area. Video resolution is 1920 × 1080.

From here, we make train val and test sets for the videos by the following rule. For each folder/place/condition, we roughly take 70:20:10 for train val and test sets.
</details>

## Acknowledgements

This codebase is built on top of https://github.com/meituan/YOLOv6.