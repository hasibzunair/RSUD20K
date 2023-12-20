# val
python tools/eval.py --data data/bdss.yaml  --weights runs/train/exp/weights/best_ckpt.pt --task val --device 0
# test
python tools/eval.py --data data/bdss.yaml  --weights runs/train/exp/weights/best_ckpt.pt --task test --save_dir runs/test/ --device 0
# get bbox preds from test
python tools/infer.py --weights runs/train/exp/weights/best_ckpt.pt --yaml data/bdss.yaml --source ../datasets/bdss5k/images/test  --device 0