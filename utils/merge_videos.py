import cv2

# Load two videos
video1 = cv2.VideoCapture('./datasets/resized_videos/IMG_7851.mp4')
video2 = cv2.VideoCapture('./datasets/resized_videos/IMG_7861.mp4')
video3 = cv2.VideoCapture('./datasets/resized_videos/IMG_8085.mp4')
video4 = cv2.VideoCapture('./datasets/resized_videos/IMG_8091.mp4')
video5 = cv2.VideoCapture('./datasets/resized_videos/IMG_8095.mp4')
video6 = cv2.VideoCapture('./datasets/resized_videos/IMG_8124.mp4')

# Get the frame size of the videos
width = int(video1.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(video1.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Create a VideoWriter object to save the result
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('output.mp4', fourcc, 30, (width*3, height*2))

# Define the titles for each video
titles = ('YOLOv6Lite-S v0', 'YOLOv6Lite-S v1', 'YOLOv6Lite-L v1')

# Merge the videos side by side
while True:
    ret1, frame1 = video1.read()
    ret2, frame2 = video2.read()
    ret3, frame3 = video3.read()
    ret4, frame4 = video4.read()
    ret5, frame5 = video5.read()
    ret6, frame6 = video6.read()
    if not ret1 or not ret2 or not ret3 or not ret4 or not ret5 or not ret6:
        break

    # Add titles to the frames
    #cv2.putText(frame1, titles[0], (10, height-30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)
    #cv2.putText(frame2, titles[1], (10, height-30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)
    #cv2.putText(frame3, titles[2], (10, height-30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)

    framex = cv2.hconcat([frame1, frame2, frame3])
    framey = cv2.hconcat([frame4, frame5, frame6])
    #print(framex.shape, framey.shape)

    framez = cv2.vconcat([framex, framey])
    out.write(framez)

# Release the resources
video1.release()
video2.release()
video3.release()
video4.release()
video5.release()
video6.release()
out.release()