import cv2
import os

from our_solutions.paths import get_name_folder_for_input_video, get_name_folder_for_output_video


video_path = get_name_folder_for_input_video()[0]
vidcap = cv2.VideoCapture(video_path)

output_folder = get_name_folder_for_output_video()
output_folder = f'{output_folder}/{os.path.basename(video_path).replace(".mp4", "")}'
output_folder = output_folder.replace(' ', '_')

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

success, image = vidcap.read()
count = 0

while success:
    cv2.imwrite(os.path.join(output_folder, f"frame_{count:04d}.png"), image)  # Сохраняем изображение в формате PNG
    success, image = vidcap.read()
    count += 1
