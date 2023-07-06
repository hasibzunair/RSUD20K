## BD StreetScenes Dataset

## 1. Specification of dependencies 

This code requires Python 3.8 and CUDA 11.6. Create and activate the following conda envrionment.

```
# Create
conda create -n bdstreets python=3.8
pip install moviepy
pip install opencv-python


# Export
conda env export > environment.yml
```


## Dataset Versions

videos: has sub folders of different places/conditions which itself has clips of different streets.

v1: train/val/test has 54//19/11 videos group partitioned in street level from `videos`.

## Project Notes

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
