import argparse
import moviepy.editor as mp
import os

""" 
Script to resize and save videos. To install run: `pip install moviepy`.

Usage: python utils/resize_and_save_videos.py --source ./datasets/videos/ --dest ./datasets/resized_videos
"""

def get_args_parser(add_help=True):
    """ Usage: args = get_args_parser()"""
    parser = argparse.ArgumentParser(description='Video Resizer', add_help=add_help)
    parser.add_argument('--source', type=str, default='data/videos', help='the destination path, e.g. video-file/dir.')
    parser.add_argument('--dest', type=str, default='data/resized_videos', help='the destination path, e.g. video-file/dir.')
    args = parser.parse_args()
    return args

args = get_args_parser()

if not os.path.exists(args.dest):
    os.makedirs(args.dest)


video_files = os.listdir(args.source)

print(video_files)

for vid_file in video_files:
    if vid_file.endswith('.MOV'):
        print(f"Processing {os.path.join(args.source, vid_file)}")

        # resize video
        clip = mp.VideoFileClip(os.path.join(args.source, vid_file))
        clip_resized = clip.resize(height=720)
        # save resized video
        vid_file = vid_file[:-3] + "mp4"
        clip_resized.write_videofile(os.path.join(args.dest, vid_file))

print("Done resizing videos.")