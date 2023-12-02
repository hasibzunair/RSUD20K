## YoloV8s

```
pip install ultralytics
```

https://github.com/ultralytics/ultralytics/issues/3920
https://docs.ultralytics.com/modes/val/#arguments

Run special commands to see version, view settings, run checks and more:

```
        yolo help
        yolo checks
        yolo version
        yolo settings
        yolo copy-cfg
        yolo cfg
```

https://github.com/ultralytics/ultralytics/blob/b6baae584c3cf8560300a8eb1c267f68e63554bb/docs/en/quickstart.md?plain=1#L189
https://github.com/ultralytics/ultralytics/blob/b6baae584c3cf8560300a8eb1c267f68e63554bb/docs/en/quickstart.md?plain=1#L189

Settings
/home/shakib/.config/Ultralytics/settings.yaml

<details>
  <summary>Validation Results</summary>

| Class         | Images | Instances | Box(P) | R     | mAP50 | mAP50-95 |
| ------------- | ------ | --------- | ------ | ----- | ----- | -------- |
| all           | 1004   | 7385      | 0.804  | 0.691 | 0.784 | 0.637    |
| person        | 1004   | 1917      | 0.896  | 0.756 | 0.883 | 0.645    |
| rickshaw      | 1004   | 1587      | 0.894  | 0.825 | 0.910 | 0.765    |
| rickshaw van  | 1004   | 240       | 0.778  | 0.667 | 0.736 | 0.482    |
| auto rickshaw | 1004   | 590       | 0.914  | 0.880 | 0.932 | 0.809    |
| truck         | 1004   | 65        | 0.636  | 0.592 | 0.668 | 0.569    |
| pickup truck  | 1004   | 74        | 0.720  | 0.676 | 0.745 | 0.578    |
| private car   | 1004   | 1420      | 0.888  | 0.806 | 0.904 | 0.771    |
| motorcycle    | 1004   | 860       | 0.896  | 0.801 | 0.904 | 0.689    |
| bicycle       | 1004   | 146       | 0.775  | 0.541 | 0.681 | 0.493    |
| bus           | 1004   | 182       | 0.831  | 0.675 | 0.801 | 0.687    |
| micro bus     | 1004   | 241       | 0.758  | 0.602 | 0.742 | 0.680    |
| covered van   | 1004   | 40        | 0.787  | 0.556 | 0.641 | 0.561    |
| human hauler  | 1004   | 23        | 0.682  | 0.609 | 0.642 | 0.552    |

</details>

<details>
  <summary>Test Results</summary>

| Class         | Images | Instances | Box(P) | R     | mAP50 | mAP50-95 |
| ------------- | ------ | --------- | ------ | ----- | ----- | -------- |
| all           | 649    | 3805      | 0.800  | 0.754 | 0.844 | 0.694    |
| person        | 649    | 844       | 0.833  | 0.819 | 0.898 | 0.702    |
| rickshaw      | 649    | 1129      | 0.854  | 0.918 | 0.963 | 0.860    |
| rickshaw van  | 649    | 83        | 0.709  | 0.747 | 0.767 | 0.528    |
| auto rickshaw | 649    | 228       | 0.891  | 0.939 | 0.964 | 0.872    |
| truck         | 649    | 29        | 0.637  | 0.586 | 0.606 | 0.500    |
| pickup truck  | 649    | 65        | 0.861  | 0.723 | 0.851 | 0.594    |
| private car   | 649    | 543       | 0.839  | 0.915 | 0.960 | 0.865    |
| motorcycle    | 649    | 509       | 0.878  | 0.886 | 0.957 | 0.751    |
| bicycle       | 649    | 121       | 0.803  | 0.776 | 0.893 | 0.694    |
| bus           | 649    | 86        | 0.773  | 0.674 | 0.826 | 0.651    |
| micro bus     | 649    | 105       | 0.901  | 0.562 | 0.834 | 0.768    |
| covered van   | 649    | 24        | 0.681  | 0.458 | 0.611 | 0.535    |
| human hauler  | 649    | 39        | 0.736  | 0.795 | 0.836 | 0.707    |

</details>

##### Acknowledgement

- [ultralytics](<>)
