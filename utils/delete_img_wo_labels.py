import os

def is_empty(file_path):
    return os.path.getsize(file_path) == 0

def delete_images_without_labels(image_folder, label_folder):
    # Get the list of image files in the image folder
    image_files = [f for f in os.listdir(image_folder) if f.endswith('.jpg') or f.endswith('.png')]  # Adjust file extensions as needed

    # Iterate through the image files
    for image_file in image_files:
        image_path = os.path.join(image_folder, image_file)
        label_path = os.path.join(label_folder, os.path.splitext(image_file)[0] + '.txt')

        # Check if the corresponding text file exists
        if not os.path.exists(label_path):
            # If the text file doesn't exist, delete the image
            os.remove(image_path)
            print(f"Deleted {image_file} because corresponding label file was not found.")
        elif is_empty(label_path):
            os.remove(image_path)
            os.remove(label_path)
            print(f"Deleted {image_file} and {label_path} because corresponding label file was empty.")

# Replace 'image_folder' and 'label_folder' with your actual folder paths
delete_images_without_labels('./datasets/tarmak_basketball_fv_datasetv0/images', './datasets/tarmak_basketball_fv_datasetv0/labels')
