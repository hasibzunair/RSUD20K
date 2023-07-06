import argparse
import os, sys
import shutil
import subprocess
import json
import cv2

"""
Code taken from https://github.com/vfdev-5/Video2Frames

Usage: python video2frames.py datasets/videos/Outdoor-FrontMin.MOV datasets/frames --maxframes=20 --verbose
"""

def vid2frames(args):

    if args.verbose:
        print( "Input arguments : ", args)

    if not os.path.exists(args.input):
        parser.error("Input video file is not found")
        return 1

    if os.path.exists(args.output):
        if args.verbose:
            print( "Remove existing output folder")
        shutil.rmtree(args.output)

    os.makedirs(args.output)

    cap = cv2.VideoCapture()
    cap.open(args.input)
    if not cap.isOpened():
        parser.error("Failed to open input video")
        return 1

    frameCount = cap.get(cv2.CAP_PROP_FRAME_COUNT)

    if args.verbose:
        print( frameCount)
    maxframes = args.maxframes
    skipDelta = 0
    if args.maxframes and frameCount > maxframes:
        skipDelta = frameCount / maxframes
        if args.verbose:
            print( "Video has {fc}, but maxframes is set to {mf}".format(fc=frameCount, mf=maxframes))
            print( "Skip frames delta is {d}".format(d=skipDelta))

    frameId = 0
    rotateAngle = args.rotate if args.rotate else 0
    if rotateAngle > 0 and args.verbose:
        print( "Rotate output frames on {deg} clock-wise".format(deg=rotateAngle))

    exif_model=None
    if args.exifmodel:
        if not os.path.exists(args.exifmodel):
            parser.error("Exif model file '{f}' is not found".format(f=args.exifmodel))
            return 2
        if args.verbose:
            print( "Use exif model from file : {f}".format(f=args.exifmodel))
        ret = subprocess.Popen(['exiftool', '-j', os.path.abspath(args.exifmodel)],
                               stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = ret.communicate()
        if args.verbose:
            print( "exiftool stdout : ", out)
        try:
            exif_model = json.loads(out)[0]
        except ValueError:
            parser.error("Exif model file can not be decoded")
            return 2

    while frameId < frameCount:
        ret, frame = cap.read()
        # print frameId, ret, frame.shape
        if not ret:
            print( "Failed to get the frame {f}".format(f=frameId))
            continue

        # Rotate if needed:
        if rotateAngle > 0:
            if rotateAngle == 90:
                frame = cv2.transpose(frame)
                frame = cv2.flip(frame, 1)
            elif rotateAngle == 180:
                frame = cv2.flip(frame, -1)
            elif rotateAngle == 270:
                frame = cv2.transpose(frame)
                frame = cv2.flip(frame, 0)

        fname = "frame_" + str(frameId) + ".jpg"
        ofname = os.path.join(args.output, fname)
        ret = cv2.imwrite(ofname, frame)
        if not ret:
            print( "Failed to write the frame {f}".format(f=frameId))
            continue

        frameId += int(1 + skipDelta)
        cap.set(cv2.CAP_PROP_POS_FRAMES, frameId)

    if exif_model:
        fields = ['Model', 'Make', 'FocalLength']
        if not write_exif_model(os.path.abspath(args.output), exif_model, fields):
            print( "Failed to write tags to the frames")
        # check on the first file
        fname = os.path.join(os.path.abspath(args.output), 'frame_0.jpg')
        cmd = ['exiftool', '-j', fname]
        for field in fields:
            cmd.append('-' + field)
        ret = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = ret.communicate()
        if args.verbose:
            print( "exiftool stdout : ", out)
        try:
            result = json.loads(out)[0]
            for field in fields:
                if field not in result:
                    parser.error("Exif model is not written to the output frames")
                    return 3
        except ValueError:
            parser.error("Output frame exif info can not be decoded")
            return 2

    return 0


def write_exif_model(folder_path, model, fields=None):
    cmd = ['exiftool', '-overwrite_original', '-r']
    for field in fields:
        if field in model:
            cmd.append('-' + field + "=" + model[field])
    cmd.append(folder_path)
    ret = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = ret.communicate()
    return ret.returncode == 0 and len(err) == 0


if __name__ == "__main__":

    print( "Start Video2Frames script ...")

    parser = argparse.ArgumentParser(description="Video2Frames converter")
    parser.add_argument('input', metavar='<input_video_file>', help="Input video file")
    parser.add_argument('output', metavar='<output_folder>', help="Output folder. If exists it will be removed")
    parser.add_argument('--maxframes', type=int, help="Output max number of frames")
    parser.add_argument('--rotate', type=int, choices={90, 180, 270}, help="Rotate clock-wise output frames")
    parser.add_argument('--exifmodel', help="An example photo file to fill output meta-tags")
    parser.add_argument('--verbose', action='store_true', help="Enable verbose")

    args = parser.parse_args()
    ret = vid2frames(args)
    print( "End Video2Frames script ...")
    exit(ret)