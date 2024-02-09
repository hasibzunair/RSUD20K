
_base_ = 'rtmdet_tiny_syncbn_fast_8xb32-300e_coco.py'




import numpy

data_root = "../datasets_json/"

#### Define your class names here
class_name = ('person', 'rickshaw', 'rickshawvan', 'autorickshaw','truck', 'pickuptruck',
                'privatecar', 'motorcycle', 'bicycle', 'bus','microbus', 'coveredvan','humanhauler')
num_classes = len(class_name)


metainfo = dict(classes=class_name, palette = [tuple(numpy.random.randint(0, 200, size=3)) for _ in range(num_classes)])

num_epochs_stage2 = 5

max_epochs = 400
train_batch_size_per_gpu = 12
train_num_workers = 4
val_batch_size_per_gpu = 2
val_num_workers = 2

load_from = 'https://download.openmmlab.com/mmyolo/v0/rtmdet/rtmdet_tiny_syncbn_fast_8xb32-300e_coco/rtmdet_tiny_syncbn_fast_8xb32-300e_coco_20230102_140117-dbb1dc83.pth'  # noqa

model = dict(
    backbone=dict(frozen_stages=4),
    bbox_head=dict(head_module=dict(num_classes=num_classes)),
    train_cfg=dict(assigner=dict(num_classes=num_classes)))

train_dataloader = dict(
    batch_size=train_batch_size_per_gpu,
    num_workers=train_num_workers,
    dataset=dict(
        data_root=data_root,
        metainfo=metainfo,
        ann_file='annotations/train_rsud20k.json',
        data_prefix=dict(img='train_rsud20k/')))

val_dataloader = dict(
    batch_size=val_batch_size_per_gpu,
    num_workers=val_num_workers,
    dataset=dict(
        metainfo=metainfo,
        data_root=data_root,
        ann_file='annotations/val_rsud20k.json',
        data_prefix=dict(img='val_rsud20k/')))


param_scheduler = [
    dict(
        type='LinearLR',
        start_factor=_base_.lr_start_factor,
        by_epoch=False,
        begin=0,
        end=30),
    dict(
        # use cosine lr from 150 to 300 epoch
        type='CosineAnnealingLR',
        eta_min=_base_.base_lr * 0.05,
        begin=max_epochs // 2,
        end=max_epochs,
        T_max=max_epochs // 2,
        by_epoch=True,
        convert_to_iter_based=True),
]

_base_.custom_hooks[1].switch_epoch = max_epochs - num_epochs_stage2

val_evaluator = dict(ann_file=data_root + 'annotations/val_rsud20k.json')


default_hooks = dict(
    checkpoint=dict(interval=10, max_keep_ckpts=2, save_best='auto'),
    logger=dict(type='LoggerHook', interval=5))
train_cfg = dict(max_epochs=max_epochs, val_interval=10)
