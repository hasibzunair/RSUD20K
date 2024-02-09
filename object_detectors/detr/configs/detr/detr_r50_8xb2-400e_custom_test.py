# The new config inherits a base config to highlight the necessary modification
_base_ = '../detr/detr_r50_8xb2-150e_coco.py'


# Modify dataset related settings
import numpy
data_root = "../datasets_json/"
metainfo = {
    'classes': ('person', 'rickshaw', 'rickshawvan', 'autorickshaw','truck', 'pickuptruck',
                'privatecar', 'motorcycle', 'bicycle', 'bus','microbus', 'coveredvan','humanhauler'),
    'palette': [
        tuple(numpy.random.randint(0, 200, size=3)) for _ in range(13)
    ]
}

# We also need to change the num_classes in head to match the dataset's annotation
model = dict(
        bbox_head=dict(num_classes=13))

test_dataloader = dict(
    dataset=dict(
        data_root=data_root,
        metainfo=metainfo,
        ann_file='annotations/test_rsud20k.json',
        data_prefix=dict(img='test_rsud20k/')))

# Modify metric related settings
test_evaluator = dict(ann_file=data_root + 'annotations/test_rsud20k.json')
