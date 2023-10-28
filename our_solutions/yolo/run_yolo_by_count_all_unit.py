from ultralytics import YOLO
import os

from our_solutions.paths import get_weight_yolo, get_path_to_input_data, \
    find_frames_rgb_paths, get_path_for_yolo_style, save_yolo_data, get_name_folder_for_pred_data

model = YOLO(get_path_for_yolo_style(get_weight_yolo(name='best_28')))

model.fuse()

n = 0
folder_path_to_rbf_input = find_frames_rgb_paths(get_path_to_input_data())
for path_to_folder in folder_path_to_rbf_input:
    for filename in os.listdir(path_to_folder):
        try:
            # print(f"{get_path_for_yolo_style(f'{path_to_folder}/{filename}')}")
            # print(f"{save_yolo_data()}/{get_name_folder_for_pred_data(path_to_folder)}/{filename}")
            results = model(
                f"{get_path_for_yolo_style(f'{path_to_folder}/{filename}')}",
                save_txt=True,
                conf=0.4,
                save_dir=f"{save_yolo_data()}/{get_name_folder_for_pred_data(path_to_folder)}")
        except FileNotFoundError:
            print("Not Found")
        break
    break
