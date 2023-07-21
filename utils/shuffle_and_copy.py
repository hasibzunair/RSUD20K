import os
import random
import shutil

# Set the directory paths
src_path = './datasets/bdss_v2/train/'
dst_path1 = './datasets/bdss_v3/train_lbl/'
dst_path2 = './datasets/bdss_v3/train_unlbl/'

# Make train sub folders
if not os.path.exists(dst_path1):
    os.makedirs(dst_path1)
if not os.path.exists(dst_path2):
    os.makedirs(dst_path2)

# Get a list of all the files in the directory
file_list = os.listdir(src_path)

# Shuffle the list of files
random.shuffle(file_list)

# Loop through the shuffled list of files
# labeled
for file_name in file_list[:5000]:
    src_file = os.path.join(src_path, file_name)
    dst_file = os.path.join(dst_path1, file_name)
    #print(dst_file)
    shutil.copy(src_file, dst_file)

# unlabeled
for file_name in file_list[5000:]:
    src_file = os.path.join(src_path, file_name)
    dst_file = os.path.join(dst_path2, file_name)
    #print(dst_file)
    shutil.copy(src_file, dst_file)