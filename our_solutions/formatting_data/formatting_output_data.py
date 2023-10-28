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


def count_all_wastes(class_counts, output_file, divider):
    with open(output_file, 'r') as f:
        lines = f.readlines()
        for id_line, line in enumerate(lines):
            if id_line in range(0, 4):
                class_counts[id_line] += int(line) // divider
    return class_counts

def generate_txt_all_wastes(output_folder_path, class_counts):
    name_file_to_save = f"frames_output.txt"
    with open(os.path.join(output_folder_path, name_file_to_save), 'w') as file:
        for count in class_counts:
            file.write(f'{count}\n')


if __name__ == '__main__':
    for root, dirs, files in os.walk(get_path_to_folder_for_predict_data()):
        class_counts = [0, 0, 0, 0]
        if len(files) != 0:
            final_path_to_count_all = ''
            for index_file, file in enumerate(files):
                file_path = os.path.join(root, file)
                counts = count_class_values(file_path)
                name_new_folder = os.path.basename(root)
                output_folder_path = get_path_to_folder_for_out_data(name_new_folder)
                final_path_to_count_all = output_folder_path
                if not os.path.exists(output_folder_path):
                    os.makedirs(output_folder_path)
                frames_output_path = f'{output_folder_path}/output'
                if not os.path.exists(frames_output_path):
                    os.makedirs(frames_output_path)
                output_file = os.path.join(frames_output_path, f'{file}')
                write_counts_to_file(counts, output_file)
                if (index_file + 1) % 23 == 0:
                    class_counts = count_all_wastes(class_counts, output_file, 1)
                elif (index_file + 1) == len(files):
                    class_counts = count_all_wastes(class_counts, output_file, 2)
            generate_txt_all_wastes(final_path_to_count_all, class_counts)
