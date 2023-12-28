import os
import shutil

train_path = './save_train_image/'
val_path = './save_val_image/'

with open("./image_number.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        a = line.split('/')
        # For traing image
        if a[4] == 'train':
            train_img = a[5].split('.') 

            for p in os.listdir(train_path):
                all_train_images = p.split('.')
                if train_img[0] == all_train_images[0]:
                    shutil.copy(train_path+all_train_images[0]+'.jpg', './large_image/')

        # For val image
        if a[4] == 'val':
            val_image = a[5].split('.') 

            for p in os.listdir(val_path):
                all_val_image = p.split('.')
                if val_image[0] == all_val_image[0]:
                    shutil.copy(val_path+all_val_image[0]+'.jpg', './large_image/')



