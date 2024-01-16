
import os
from PIL import Image
from tqdm import tqdm

test_image_path = '../datasets/bdss20k/images/test/'

count= 0
# List of images to process
image_names = [name for name in os.listdir(test_image_path) if name.lower().endswith(('.png', '.jpg', '.jpeg'))]

# Initialize tqdm progress bar
with tqdm(total=len(image_names), unit='img') as pbar:
    for image_name in image_names:
        image_path = os.path.join(test_image_path, image_name)
        try:
            count += 1
            # print(count)
            
            # Update progress bar description with success message
            pbar.set_description(f"Image Saved")
        except Exception as e:
            # Update progress bar description with error message
            pbar.set_description(f"Error {image_name}")

        # Update the progress bar by one step
        pbar.update(1)
print(count)