import os

def rename_files(image_folder, label_folder):
    # Rename image files
    image_files = [f for f in os.listdir(image_folder) if f.endswith('.jpg') or f.endswith('.png')]  # Adjust file extensions as needed
    for i, image_file in enumerate(image_files):
        current_image_path = os.path.join(image_folder, image_file)
        new_image_name = f"train{i}.jpg"
        new_image_path = os.path.join(image_folder, new_image_name)
        os.rename(current_image_path, new_image_path)
        print(f"Renamed {image_file} to {new_image_name}")

    # Rename label files
    label_files = [f for f in os.listdir(label_folder) if f.endswith('.txt')]
    for i, label_file in enumerate(label_files):
        current_label_path = os.path.join(label_folder, label_file)
        new_label_name = f"train{i}.txt"
        new_label_path = os.path.join(label_folder, new_label_name)
        os.rename(current_label_path, new_label_path)
        print(f"Renamed {label_file} to {new_label_name}")

# Replace 'image_folder' and 'label_folder' with your actual folder paths
image_folder_path = 'path_to_images'
label_folder_path = 'path_to_labels'

rename_files(image_folder_path, label_folder_path)