import cv2
import numpy as np

def resize_video(video_path, target_width, target_height):
    """Resize a video to the target width and height."""
    cap = cv2.VideoCapture(video_path)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    aspect_ratio = width / height

    # Calculate new dimensions while maintaining the aspect ratio
    if target_width / target_height > aspect_ratio:
        new_width = int(target_height * aspect_ratio)
        new_height = target_height
    else:
        new_width = target_width
        new_height = int(target_width / aspect_ratio)

    resized_frames = []
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Resize each frame
        resized_frame = cv2.resize(frame, (new_width, new_height))
        resized_frames.append(resized_frame)

    cap.release()
    return resized_frames

def create_video_collage(video_paths, output_path):
    """Create a video collage from six input videos using OpenCV."""
    # Define the grid layout (2 rows, 3 columns)
    grid_layout = (2, 3)

    # Define target width and height for each video in the collage
    target_width = 150
    target_height = 80

    # Resize videos to the target dimensions
    resized_videos = [resize_video(path, target_width, target_height) for path in video_paths]

    # Ensure all videos have the same number of frames (trim if necessary)
    min_frames = min(len(frames) for frames in resized_videos)
    resized_videos = [frames[:min_frames] for frames in resized_videos]

    # Combine frames into a video collage
    collage_frames = np.concatenate([np.concatenate(row, axis=1) for row in resized_videos], axis=0)

    # Write the collage frames to a video file
    print(collage_frames.shape[1], collage_frames.shape[0])
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_path, fourcc, 24, (collage_frames.shape[1], collage_frames.shape[0]))

    for frame in collage_frames:
        out.write(frame)

    out.release()

if __name__ == "__main__":
    # Provide paths to six input videos
    video_paths = [
        "./datasets/resized_videos/IMG_7851.mp4",
        "./datasets/resized_videos/IMG_7861.mp4",
        "./datasets/resized_videos/IMG_8085.mp4",
        "./datasets/resized_videos/IMG_8091.mp4",
        "./datasets/resized_videos/IMG_8095.mp4",
        "./datasets/resized_videos/IMG_8124.mp4",
    ]

    # Specify the output path for the collage video
    output_path = "./datasets/resized_videos/video_collage.mp4"

    # Create the video collage
    create_video_collage(video_paths, output_path)