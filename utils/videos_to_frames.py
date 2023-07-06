import os
import argparse
import shutil

from video2frames import vid2frames

""" 
Script that:
read resized videos
put frames in separate folders
put all files in one folder
delete the separate folders

Usage:
# python utils/videos_to_frames.py --source ./datasets/resized_videos/ --dest ./datasets/frames --maxframes 10
"""

def get_args_parser(add_help=True):
    """ Usage: args = get_args_parser()"""
    parser = argparse.ArgumentParser(description='Video Resizer', add_help=add_help)
    parser.add_argument('--source', type=str, default='data/videos', help='the destination path, e.g. video-file/dir.')
    parser.add_argument('--dest', type=str, default='data/frames', help='the destination path, e.g. image-file/dir.')
    
    # for video2frames function
    parser.add_argument('input', default='data/videos.mp4', nargs='?', const=1, help="Input video file")
    parser.add_argument('output', default='data/frames', nargs='?', const=1, help="Output folder. If exists it will be removed")
    parser.add_argument('--maxframes', type=int, help="Output max number of frames")
    parser.add_argument('--rotate', type=int, choices={90, 180, 270}, help="Rotate clock-wise output frames")
    parser.add_argument('--exifmodel', help="An example photo file to fill output meta-tags")
    parser.add_argument('--verbose', action='store_true', help="Enable verbose")
    args = parser.parse_args()
    return args

args = get_args_parser()

video_files = os.listdir(args.source)


# Get frames from videos
for ct, vid_file in enumerate(video_files):
    if vid_file.endswith('.mp4'):
        vid_file_path = os.path.join(args.source, vid_file)
        print(f"Processing {vid_file_path}")

        # Make folder for video frames
        if not os.path.exists(f"{args.dest}"):
            os.makedirs(f"{args.dest}")
        if not os.path.exists(f"{args.dest}/{ct}"):
            os.makedirs(f"{args.dest}/{ct}")

        args.input = vid_file_path
        args.output = f"{args.dest}/{ct}"

        # Convert to frames
        ret = vid2frames(args)

# Rename all files in subfolders
frame_sub_folders = os.listdir(args.dest)
print(frame_sub_folders)

# Stores content of all the listed folders in the dictionary with folder name as key and its content as a value list.
folder_contents = {}
for folder in frame_sub_folders:
    folder_contents[folder] = os.listdir(os.path.join(args.dest, folder))

# Loop through the dictionary with all the folders.
# Now loop through the content of each folder and one by one move them to the merge folder.
ct = 0
for folder, contents in folder_contents.items():
    for content in contents:
        src_file = os.path.join(args.dest, folder, content)        
        os.rename(src_file, os.path.join(args.dest, folder, f"{ct}.jpg"))
        src_file_rename = os.path.join(args.dest, folder, f"{ct}.jpg")
        dst_file_rename = os.path.join(args.dest, f"{ct}.jpg")
        
        # move file
        shutil.move(src_file_rename, dst_file_rename)
        ct+=1

# Delete sub folders
for folder in frame_sub_folders:
    os.rmdir(os.path.join(args.dest, folder))