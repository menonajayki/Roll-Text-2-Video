from nltk.tokenize import sent_tokenize
import cv2
import numpy as np
def text_to_video(text, output_video):
    sentences = sent_tokenize(text)
    width, height = 640, 480
    fps = 24
    duration_per_sentence = 3
    num_frames_per_move = int(fps * duration_per_sentence)
    distance_to_move_per_frame = int(width / (num_frames_per_move * 2))

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_video, fourcc, fps, (width, height))

    for sentence in sentences:
        img = np.zeros((height, width, 3), np.uint8)
        img.fill(255)
        font = cv2.FONT_ITALIC
        fontScale = 1
        fontColor = (0, 0, 0)
        lineType = 2

        for frame_num in range(num_frames_per_move):
            img_copy = img.copy()
            x_position = frame_num * distance_to_move_per_frame
            bottomLeftCornerOfText = (x_position, height // 2)
            cv2.putText(img_copy, sentence, bottomLeftCornerOfText, font, fontScale, fontColor, lineType)
            out.write(img_copy)
    out.release()

text = ("""Hello This  is my frame 1. This is frame 2. This is 3""")
output_video = "output_video.mp4"
text_to_video(text, output_video)
