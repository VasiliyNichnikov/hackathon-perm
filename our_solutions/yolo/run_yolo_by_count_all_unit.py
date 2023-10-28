from pathlib import Path

from ultralytics import YOLO
import os

from our_solutions.paths import get_weight_yolo, \
    find_frames_rgb_paths, get_path_for_yolo_style, get_output_yolo_data_path, get_name_folder_for_pred_data

model = YOLO(get_path_for_yolo_style(get_weight_yolo(name='best_28')))

model.fuse()

n = 0
folder_path_to_rbf_input = find_frames_rgb_paths()
for path_to_folder in folder_path_to_rbf_input:
    for filename in os.listdir(path_to_folder):
        try:
            path_folder = Path(path_to_folder).parent
            if not os.path.exists(path_folder):
                print("Error")
                continue

            last_folder_name = path_folder.name.split('/')[-1]
            input_path = os.path.join(path_to_folder, filename)
            output_path_folder = get_output_yolo_data_path(last_folder_name)
            output_path_name = os.path.join(output_path_folder, filename.replace(".png", ".txt"))

            if not os.path.exists(output_path_folder):
                os.makedirs(output_path_folder)

            results = model(input_path,  conf=0.4, project="ass")
            for result in results:
                result.save_txt(output_path_name)
        except FileNotFoundError:
            print(f"Not found path: {filename}")