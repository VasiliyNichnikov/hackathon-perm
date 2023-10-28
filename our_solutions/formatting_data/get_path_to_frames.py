import os

from our_solutions.paths import get_path_to_input_data


def find_frames_rgb_paths(root_dir):
    frames_rgb_paths = []
    for root, dirs, files in os.walk(root_dir):
        if 'frames_rgb' in dirs:
            frames_rgb_paths.append(os.path.join(root, 'frames_rgb'))
    return frames_rgb_paths
