## BD StreetScenes Dataset

This repo is for BD StreetScenes Dataset.

## 1. Specification of dependencies 

This code requires Python 3.8 and CUDA 11.4. Create and activate the following conda envrionment.

```
# Create fresh env
conda create -n bdstr python=3.8
conda install pytorch torchvision torchaudio cudatoolkit=11.1 -c pytorch-lts -c nvidia
pip install moviepy
pip install opencv-python


# Export
conda env export > environment.yml
```


## Dataset Versions

videos: has sub folders of different places/conditions which itself has clips of different streets.

v1: train/val/test has 54//19/11 videos group partitioned in street level from `videos`.

v2: train/val/test has frames from `v1`.

## Project Notes

**[July 14, 2023]** Get frames from videos.

```
python utils/videos_to_frames.py --source ./datasets/v1/test --dest ./datasets/v2/test --maxframes 10
python utils/videos_to_frames.py --source ./datasets/v1/val --dest ./datasets/v2/val --maxframes 10
python utils/videos_to_frames.py --source ./datasets/v1/train --dest ./datasets/v2/train --maxframes 10
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
