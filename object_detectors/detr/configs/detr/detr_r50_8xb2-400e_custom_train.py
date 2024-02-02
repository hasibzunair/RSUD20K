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


train_dataloader = dict(
    batch_size=1,
    dataset=dict(
        data_root=data_root,
        metainfo=metainfo,
        ann_file='annotations/train_rsud20k.json',
        data_prefix=dict(img='train_rsud20k/')))

val_dataloader = dict(
    dataset=dict(
        data_root=data_root,
        metainfo=metainfo,
        ann_file='annotations/val_rsud20k.json',
        data_prefix=dict(img='val_rsud20k/')))

# Modify metric related settings
val_evaluator = dict(ann_file=data_root + 'annotations/val_rsud20k.json')


# We can use the pre-trained Mask RCNN model to obtain higher performance
load_from = 'https://download.openmmlab.com/mmdetection/v3.0/detr/detr_r50_8xb2-150e_coco/detr_r50_8xb2-150e_coco_20221023_153551-436d03e8.pth'

# learning policy
max_epochs = 400
train_cfg = dict(
    type='EpochBasedTrainLoop', max_epochs=max_epochs, val_interval=10)


param_scheduler = [
    dict(
        type='MultiStepLR',
        begin=0,
        end=max_epochs,
        by_epoch=True,
        milestones=[334],
        gamma=0.1)
]

# only keep latest 5 checkpoints
default_hooks = dict(checkpoint=dict(max_keep_ckpts=5))
