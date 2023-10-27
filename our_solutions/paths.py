import os
from pathlib import Path


def get_project_root():
    return Path(__file__).parent


def get_no_sorted_data_path(name):
    return os.path.join(get_project_root(), f'static/raw_data/{name}.txt')


def get_path_to_folder_for_transformed_data(name):
    return os.path.join(get_project_root(), f'static/transformed_data/{name}')
