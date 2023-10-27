import os
from pathlib import Path


def get_project_root():
    return Path(__file__).parent.parent.parent


def get_no_sorted_data_path(name):
    return os.path.join(get_project_root(), f'static/{name}.txt')
