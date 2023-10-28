import os

from our_solutions.paths import get_path_to_folder_for_out_data, get_path_to_folder_for_predict_data


def count_class_values(file_path):
    class_counts = {0: 0, 1: 0, 2: 0, 3: 0}
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            elements = line.split()
            class_counts[int(elements[0])] += 1
    return class_counts


def write_counts_to_file(counts, output_file):
    with open(output_file, 'w') as file:
        for count in counts.values():
            file.write(f'{count}\n')


if __name__ == '__main__':
    for root, dirs, files in os.walk(get_path_to_folder_for_predict_data()):
        for file in files:
            file_path = os.path.join(root, file)
            counts = count_class_values(file_path)
            name_new_folder = os.path.basename(root)
            output_folder_path = get_path_to_folder_for_out_data(name_new_folder)
            if not os.path.exists(output_folder_path):
                os.makedirs(output_folder_path)
            output_file = os.path.join(output_folder_path, f'{file}')
            write_counts_to_file(counts, output_file)
