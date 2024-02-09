import os
import random
import torch
import argparse
import numpy as np
from ultralytics import YOLO

########## Reproducibility ##########
random.seed(0)
np.random.seed(0)
os.environ["PYTHONHASHSEED"] = str(0)
torch.manual_seed(0)
torch.cuda.manual_seed(0)
torch.cuda.manual_seed_all(0)
if torch.cuda.is_available():
    torch.backends.cudnn.deterministic = True
torch.backends.cudnn.benchmark = True


def Args():
    parser = argparse.ArgumentParser(description='Train YOLOv8m model with PyTorch.')
    parser.add_argument('--yaml_path', default='./data/rsud20k.yaml', type=str, help='Path to the dataset YAML file.')
    parser.add_argument('--img_size', default=640, type=int, help='Image size (pixels) for training and validation.')
    parser.add_argument('--batch_size', default=12, type=int, help='Total batch size for training.')
    parser.add_argument('--epochs', default=400, type=int, help='Number of epochs to run during training.')
    parser.add_argument('--device', default=0, type=str, help='CUDA device(s) i.e 0,1,2 to use or "cpu" for CPU training.')
    args = parser.parse_args()
    return args


def main():
    args = Args()
    
    # Validate YAML path
    if not os.path.isfile(args.yaml_path):
        raise FileNotFoundError(f"The specified YAML file was not found: {args.yaml_path}")

    # Load a pretrained YOLOv8m model
    model = YOLO('yolov8m.pt')

    # Train the model using the specified dataset
    try:
        with torch.cuda.device(args.device):
            model.train(data=args.yaml_path, imgsz=args.img_size, epochs=args.epochs, batch=args.batch_size, device=args.device)
    except Exception as e:
        print(f"An error occurred during training: {e}")

    # Validate the model
    try:
        metrics = model.val()  # Dataset and settings are remembered from training
        print(f"mAP50-95: {metrics.box.map}")
        print(f"mAP50: {metrics.box.map50}")
        print(f"mAP75: {metrics.box.map75}")
        print(f"mAP50-95 per category: {metrics.box.maps}")
    except Exception as e:
        print(f"An error occurred during validation: {e}")


if __name__ == "__main__":
    main()
    


