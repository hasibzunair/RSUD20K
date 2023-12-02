import argparse
import os

from PIL import Image

from ultralytics import YOLO

# Main function
if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Evaluate and test YOLOv8s model on a test dataset."
    )
    parser.add_argument(
        "--weights",
        type=str,
        default="runs/detect/train/weights/best.pt",
        help="Path to the model weights file.",
    )
    parser.add_argument(
        "--yaml_path",
        default="./data/bdss20k.yaml",
        type=str,
        help="Path to the dataset YAML file.",
    )
    parser.add_argument(
        "--test_image_path",
        default="../datasets/bdss20k/images/test/",
        type=str,
        help="Path to test data images.",
    )
    parser.add_argument(
        "--img_size", default=640, type=int, help="Image size (pixels) for inference."
    )
    parser.add_argument(
        "--batch_size", default=12, type=int, help="Batch size for inference."
    )
    parser.add_argument(
        "--epochs", default=400, type=int, help="Number of epochs for model evaluation."
    )
    parser.add_argument(
        "--device", default=0, type=str, help='CUDA device(s) to use or "cpu" for CPU.'
    )
    parser.add_argument(
        "--save_dir",
        default="predictions/",
        type=str,
        help="Directory to save prediction images.",
    )
    args = parser.parse_args()

    # Load the model with specified weights
    model = YOLO(args.weights)

    # Evaluate the model on the test dataset
    try:
        metrics = model.val(
            data=args.yaml_path,
            imgsz=args.img_size,
            batch=args.batch_size,
            split="test",
            device=args.device,
        )
        print(f"mAP@50-95: {metrics.box.map}")
        print(f"mAP@50: {metrics.box.map50}")
        print(f"mAP@75: {metrics.box.map75}")
        print(f"mAP@50:95 per category: {metrics.box.maps}")
    except Exception as e:
        print(f"An error occurred during evaluation: {e}")

    # Ensure the save directory exists
    os.makedirs(args.save_dir, exist_ok=True)

    # Predict and save images
    for image_name in os.listdir(args.test_image_path):
        image_path = os.path.join(args.test_image_path, image_name)
        if image_name.lower().endswith((".png", ".jpg", ".jpeg")):
            try:
                results = model.predict(image_path)
                result_image = Image.fromarray(results[0].plot()[:, :, ::-1])
                save_path = os.path.join(args.save_dir, image_name)
                result_image.save(save_path)
                print(f"Saved prediction for {image_name} at {save_path}")
            except Exception as e:
                print(f"An error occurred while processing {image_name}: {e}")
