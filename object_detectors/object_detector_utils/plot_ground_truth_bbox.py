# -*- coding:utf-8 -*-
import os
import cv2
import time
import math
import torch
import random
import argparse
import numpy as np
import os.path as osp

from tqdm import tqdm
from pathlib import Path
from PIL import ImageFont
from collections import deque

parser = argparse.ArgumentParser(description="Plot the ground truth boxes on the images.")
parser.add_argument('--data_path', type=str, default='../datasets/rsud20k',
                    help='Path to the dataset.')
parser.add_argument('--data', type=str, default='test',
                    help='Name of the data folder.')
parser.add_argument('--output_image_folder', type=str, default='./save_image/',
                    help='Path to the output images.')
parser.add_argument('--class_file', type=str, default='../datasets/rsud20k/classes.txt',
                    help='Path to the file containing class names.')
args = parser.parse_args()


# Config the global variables 
RAW_IMAGE_FOLDER = os.path.join(args.data_path, 'images/'+ args.data)
LABEL_FOLDER = os.path.join(args.data_path, 'labels/'+args.data)  
OUTPUT_IMAGE_FOLDER = f'save_{args.data}_image/'  # The output images would be saved to this folder.
IMAGE_NAME_LIST_PATH = f'{args.data}_name_list.txt'  # The file name of images will be saved into this text file.
CLASS_PATH = args.class_file  # The file containing class names.

if not os.path.exists(OUTPUT_IMAGE_FOLDER):
    os.makedirs(OUTPUT_IMAGE_FOLDER)


def generate_colors(i, bgr=False):
    hex = ('FF3838', 'FF9D97', 'FF701F', 'FFB21D', 'CFD231', '48F90A', '92CC17', '3DDB86', '1A9334', '00D4BB',
            '2C99A8', '00C2FF', '344593', '6473FF', '0018EC', '8438FF', '520085', 'CB38FF', 'FF95C8', 'FF37C7')
    palette = []
    for iter in hex:
        h = '#' + iter
        palette.append(tuple(int(h[1 + i:1 + i + 2], 16) for i in (0, 2, 4)))
    color = palette[i]
    return (color[2], color[1], color[0])

def font_check(font='./Arial.ttf', size=10):
    # Return a PIL TrueType Font, downloading to CONFIG_DIR if necessary
    assert osp.exists(font), f'font path not exists: {font}'
    try:
        return ImageFont.truetype(str(font) if font.exists() else font.name, size)
    except Exception as e:  # download if missing
        return ImageFont.truetype(str(font), size)

def plot_box_and_label(image, lw, box, label='', color=(128, 128, 128), txt_color=(255, 255, 255), font=cv2.FONT_HERSHEY_COMPLEX):
    # Add one xyxy box to image with label
    label = label + '  ' if label else ''
    p1, p2 = (int(box[0]), int(box[1])), (int(box[2]), int(box[3]))
    cv2.rectangle(image, p1, p2, color, thickness=lw, lineType=cv2.LINE_AA)
    if label:
        tf = max(lw - 1, 1)  # font thickness
        w, h = cv2.getTextSize(label, 0, fontScale=lw / 3, thickness=tf)[0]  # text width, height
        outside = p1[1] - h - 3 >= 0  # label fits outside box
        p2 = p1[0] + w, p1[1] - h - 3 if outside else p1[1] + h + 3
        cv2.rectangle(image, p1, p2, color, -1, cv2.LINE_AA)  # filled
        cv2.putText(image, label, (p1[0], p1[1] - 2 if outside else p1[1] + h + 2), 
                    font, 
                    lw / 3, 
                    txt_color,
                    thickness=tf, lineType=cv2.LINE_AA)



def draw_box_on_image(image_name, classes, LABEL_FOLDER, RAW_IMAGE_FOLDER, OUTPUT_IMAGE_FOLDER):
    """
    This function will add rectangle boxes on the images.
    """
    txt_path = os.path.join(LABEL_FOLDER, '%s.txt' %
                            (image_name))  
    print(image_name)
    if image_name == '.DS_Store':
        return 0
    image_path = os.path.join(RAW_IMAGE_FOLDER, '%s.jpg' %
                              (image_name))  

    save_file_path = os.path.join(
        OUTPUT_IMAGE_FOLDER, '%s.jpg' % (image_name)) 

   
    source_file = open(txt_path) if os.path.exists(txt_path) else []
    image = cv2.imread(image_path)
    try:
        height, width, channels = image.shape
    except:
        print('no shape info.')
        return 0

    box_number = 0
    for line in source_file:  
        staff = line.split()  
        class_idx = int(staff[0])

        x_center, y_center, w, h = float(
            staff[1])*width, float(staff[2])*height, float(staff[3])*width, float(staff[4])*height
        x1 = round(x_center-w/2)
        y1 = round(y_center-h/2)
        x2 = round(x_center+w/2)
        y2 = round(y_center+h/2)
    
        plot_box_and_label(image, max(round(sum(image.shape) / 2 * 0.003), 2), [x1, y1, x2, y2], label=classes[class_idx], color=generate_colors(class_idx, True))

        cv2.imwrite(save_file_path, image)

        box_number += 1
    
    return box_number

def make_name_list(RAW_IMAGE_FOLDER, IMAGE_NAME_LIST_PATH):
    """
    if you want to save the image names into a text file, you can use this function.  
    This function will collect the image names without extension and save them in the name_list.txt. 
    """
    image_file_list = os.listdir(RAW_IMAGE_FOLDER)  

    text_image_name_list_file = open(
        IMAGE_NAME_LIST_PATH, 'w')  

    for image_file_name in image_file_list:  
        image_name, file_extend = os.path.splitext(image_file_name) 
        text_image_name_list_file.write(image_name+'\n')  

    text_image_name_list_file.close()

if __name__ == '__main__':           

    make_name_list(RAW_IMAGE_FOLDER, IMAGE_NAME_LIST_PATH)

    classes = image_names = open(CLASS_PATH).read().strip().split('\n')
    random.seed(42)
    image_names = open(IMAGE_NAME_LIST_PATH).read(
    ).strip().split()  
    box_total = 0
    image_total = 0
    for image_name in image_names:
        box_num = draw_box_on_image(
            image_name, classes, LABEL_FOLDER, RAW_IMAGE_FOLDER, OUTPUT_IMAGE_FOLDER)  
        box_total += box_num
        image_total += 1
        print('Box number:', box_total, 'Image number:', image_total)
    
    print("Completed!!!")
