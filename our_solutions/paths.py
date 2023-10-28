import os
from pathlib import Path


def get_project_root():
    return Path(__file__).parent


def get_no_sorted_data_path(name):
    return os.path.join(get_project_root(), f'static/raw_data/{name}.txt')


def get_path_to_folder_for_transformed_data(name):
    return os.path.join(get_project_root(), f'static/transformed_data/{name}')


def get_path_to_folder_for_predict_data():
    directory = 'static/runs_predict'
    if not os.path.exists(directory):
        os.makedirs(directory)
    return os.path.join(get_project_root(), f'static/runs_predict')


def get_path_to_folder_for_predict_data_for_all_frames():
    return os.path.join(get_project_root(), f'static/runs_predict_for_all_frame')


def get_path_to_folder_for_out_data(name):
    directory = 'static/out_data'
    if not os.path.exists(directory):
        os.makedirs(directory)
    return os.path.join(get_project_root(), f'{directory}/{name}')


def get_path_to_folder_for_out_data_for_all_frame(name):
    directory = 'static/out_data_for_all_frame'
    if not os.path.exists(directory):
        os.makedirs(directory)
    return os.path.join(get_project_root(), f'{directory}/{name}')


def get_path_to_folder_data_rgb(name):
    return os.path.join(get_project_root(), f'static/input_data/{name}')


def get_weight_yolo(name):
    return os.path.join(get_project_root(), f'static/yolo_weight/{name}.pt')


def get_path_to_input_data():
    return os.path.join(get_project_root(), f'static/input_data')


def find_frames_rgb_paths() -> list[str]:
    frames_rgb_paths = []
    for root, dirs, files in os.walk(get_path_to_input_data()):
        if 'frames_rgb' in dirs:
            frames_rgb_paths.append(get_path_for_yolo_style(os.path.join(root, 'frames_rgb')))
    return frames_rgb_paths


def get_path_for_yolo_style(path):
    return path.replace("\\", '/')


def get_output_yolo_data_path(name: str) -> str:
    path_folder = os.path.join(get_project_root(), f'static/runs_predict')
    if not os.path.exists(path_folder):
        os.makedirs(path_folder)
    file_path = os.path.join(path_folder, name)
    return get_path_for_yolo_style(file_path)


def runs_predict_for_all_frame(name: str) -> str:
    path_folder = os.path.join(get_project_root(), f'static/runs_predict_for_all_frame')
    if not os.path.exists(path_folder):
        os.makedirs(path_folder)
    file_path = os.path.join(path_folder, name)
    return get_path_for_yolo_style(file_path)


def get_name_folder_for_pred_data(path):
    return os.path.basename(os.path.normpath(os.path.dirname(path)))

def get_name_folder_for_input_video():
    directory = os.path.join(get_project_root(), f'static/input_video')
    if not os.path.exists(directory):
        os.makedirs(directory)
    file_list = []
    for file in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, file)):
            file_list.append(f'{directory}/{file}')
    return file_list

def get_name_folder_for_output_video():
    output_folder = os.path.join(get_project_root(), f'static/output_video')
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    return os.path.join(output_folder)