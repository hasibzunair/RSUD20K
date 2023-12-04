import os
import argparse
from ultralytics import YOLO
from PIL import Image


# Main function
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Evaluate and test YOLOv8m model on a test dataset.')
    parser.add_argument('--weights', type=str, default='runs/detect/train/weights/best.pt', help='Path to the model weights file.')
    parser.add_argument('--yaml_path', default='./data/bdss20k.yaml', type=str, help='Path to the dataset YAML file.')
    parser.add_argument('--img_size', default=640, type=int, help='Image size (pixels) for inference.')
    parser.add_argument('--batch_size', default=12, type=int, help='Batch size for inference.')
    parser.add_argument('--device', default=0, type=str, help='CUDA device(s) to use or "cpu" for CPU.')
    args = parser.parse_args()

    # Load the model with specified weights
    model = YOLO(args.weights)
    
    # Evaluate the model on the test dataset
    try:
        metrics = model.val(data=args.yaml_path, imgsz=args.img_size, batch=args.batch_size, split='test', device=args.device)
        print(f"mAP@50-95: {metrics.box.map}")
        print(f"mAP@50: {metrics.box.map50}")
        print(f"mAP@75: {metrics.box.map75}")
        print(f"mAP@50:95 per category: {metrics.box.maps}")
    except Exception as e:
        print(f"An error occurred during evaluation: {e}")




