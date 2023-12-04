import os
import argparse
from ultralytics import YOLO
from PIL import Image


# Main function
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Evaluate and test YOLOv8m model on a test dataset.')
    parser.add_argument('--weights', type=str, default='runs/detect/train/weights/best.pt', help='Path to the model weights file.')
    parser.add_argument('--test_image_path', default='../datasets/bdss20k/images/test/', type=str, help='Path to test data images.')
    parser.add_argument('--save_dir', default='predictions/', type=str, help='Directory to save prediction images.')
    args = parser.parse_args()

    # Load the model with specified weights
    model = YOLO(args.weights)
    
    # Ensure the save directory exists
    os.makedirs(args.save_dir, exist_ok=True)

    # Predict and save images
    for image_name in os.listdir(args.test_image_path):
        image_path = os.path.join(args.test_image_path, image_name)
        if image_name.lower().endswith(('.png', '.jpg', '.jpeg')):
            try:
                results = model.predict(image_path)
                result_image = Image.fromarray(results[0].plot()[:, :, ::-1])
                save_path = os.path.join(args.save_dir, image_name)
                result_image.save(save_path)
                print(f"Saved prediction for {image_name} at {save_path}")
            except Exception as e:
                print(f"An error occurred while processing {image_name}: {e}")

