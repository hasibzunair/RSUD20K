import gradio as gr
import cv2
import codecs
import os
from PIL import Image
from ultralytics import YOLO


################## MODEL ##################
model = YOLO('best.pt')
title = "RSUD20K: A Dataset for Road Scene Understanding In Autonomous Driving"
description = codecs.open("description.html", "r", "utf-8").read()

################## IMAGE ##################

Image_directory = "examples/images"

inputs_image = [
    gr.components.Image(type="filepath", label="Input Image"),
]
outputs_image = [
    gr.components.Image(type="numpy", label="Output Image"),
]

def show_preds_image(image_path):
    image = cv2.imread(image_path)
    outputs = model.predict(source=image_path)
    results = Image.fromarray(outputs[0].plot()[:, :, ::-1])
    return results

    
demo_image = gr.Interface(
    fn=show_preds_image,
    title=title,
    description=description,
    inputs= inputs_image,
    outputs= outputs_image,
    examples= [os.path.join(Image_directory, fname) for fname in os.listdir(Image_directory) if fname.endswith(".jpg")],
    allow_flagging="never",
    analytics_enabled=False,
)

################## VIDEO ##################

Video_directory = "examples/videos"

inputs_video = [
    gr.components.Video(label="Input Video"),
]

outputs_video = [
    gr.components.Image(type = "numpy", label="Output Video"),
]


def show_preds_video(video_path):
    cap = cv2.VideoCapture(video_path)
    predicted_frames = []
    while(cap.isOpened()):
        ret, frame = cap.read()
        if ret:
            frame_copy = frame.copy()
            outputs = model.predict(source=frame)
            results = Image.fromarray(outputs[0].plot()[:, :, ::-1])
            yield results
        else:
            break
    cap.release()
    cv2.destroyAllWindows()

demo_video = gr.Interface(
    fn=show_preds_video,
    title=title,
    description=description,
    inputs= inputs_video,
    outputs= outputs_video,
    examples= [os.path.join(Video_directory, fname) for fname in os.listdir(Video_directory) if fname.endswith(".mp4")],
    allow_flagging="never",
    analytics_enabled=False,
)

################## LAUNCH ##################
gr.TabbedInterface(
    [demo_image, demo_video],
    tab_names=['Image inference', 'Video inference']
).queue().launch()