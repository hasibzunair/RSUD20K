## DETR


##### mmdetection
[![PyPI](https://img.shields.io/pypi/v/mmdet)](https://pypi.org/project/mmdet)
[![docs](https://img.shields.io/badge/docs-latest-blue)](https://mmdetection.readthedocs.io/en/latest/)
[![badge](https://github.com/open-mmlab/mmdetection/workflows/build/badge.svg)](https://github.com/open-mmlab/mmdetection/actions)
[![codecov](https://codecov.io/gh/open-mmlab/mmdetection/branch/main/graph/badge.svg)](https://codecov.io/gh/open-mmlab/mmdetection)
[![license](https://img.shields.io/github/license/open-mmlab/mmdetection.svg)](https://github.com/open-mmlab/mmdetection/blob/main/LICENSE)
[![open issues](https://isitmaintained.com/badge/open/open-mmlab/mmdetection.svg)](https://github.com/open-mmlab/mmdetection/issues)
[![issue resolution](https://isitmaintained.com/badge/resolution/open-mmlab/mmdetection.svg)](https://github.com/open-mmlab/mmdetection/issues)
[![Open in OpenXLab](https://cdn-static.openxlab.org.cn/app-center/openxlab_demo.svg)](https://openxlab.org.cn/apps?search=mmdet)

[📘Documentation](https://mmdetection.readthedocs.io/en/latest/) |
[🛠️Installation](https://mmdetection.readthedocs.io/en/latest/get_started.html) |
[👀Model Zoo](https://mmdetection.readthedocs.io/en/latest/model_zoo.html) |
[🆕Update News](https://mmdetection.readthedocs.io/en/latest/notes/changelog.html) |
[🚀Ongoing Projects](https://github.com/open-mmlab/mmdetection/projects) |
[🤔Reporting Issues](https://github.com/open-mmlab/mmdetection/issues/new/choose)

python tools/train.py configs/detr/detr_r50_8xb2-150e_custom_train.py

python tools/test.py configs/detr/detr_r50_8xb2-150e_custom_test.py work_dirs/rtmdet_tiny_fast_1xb12-40e_custom_train/epoch_1.pth --show-dir show_results --cfg-options test_evaluator.classwise=True


python tools/train.py configs/balloon/mask-rcnn_r50-caffe_fpn_ms-poly-1x_balloon.py

python tools/test.py configs/balloon/mask-rcnn_r50-caffe_fpn_ms-poly-1x_balloon.py work_dirs/mask-rcnn_r50-caffe_fpn_ms-poly-1x_balloon/epoch_12.pth