## BD StreetScenes Dataset

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

Where each folder has video clips of different streets of the same area.

From here, we make train val and test sets for the videos by the following rule. For each folder/place/condition, we roughly take 70:20:10 for train val and test sets.
