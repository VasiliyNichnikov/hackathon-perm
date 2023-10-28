import os

from our_solutions.paths import get_path_to_folder_for_out_data_for_all_frame, \
    get_path_to_folder_for_predict_data_for_all_frames


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

def count_all_wastes(output_folder_path):
    class_counts = [0, 0, 0, 0]

    for file in os.listdir(output_folder_path):
        if file.endswith(".txt"):
            with open(os.path.join(output_folder_path, file), 'r') as f:
                lines = f.readlines()
                for id_line, line in enumerate(lines):
                    if id_line in range(0, 4):
                        class_counts[id_line] += int(line)
    print(class_counts)
    folder_to_save = f'{os.path.dirname(output_folder_path)}'
    name_file_to_save = f"{os.path.basename(output_folder_path)}.txt"
    with open(os.path.join(folder_to_save, name_file_to_save), 'w') as file:
        for count in class_counts:
            file.write(f'{count}\n')


if __name__ == '__main__':
    for root, dirs, files in os.walk(get_path_to_folder_for_predict_data_for_all_frames()):
        for file in files:
            file_path = os.path.join(root, file)
            counts = count_class_values(file_path)
            name_new_folder = os.path.basename(root)
            output_folder_path = get_path_to_folder_for_out_data_for_all_frame(name_new_folder)
            if not os.path.exists(output_folder_path):
                os.makedirs(output_folder_path)
            output_file = os.path.join(output_folder_path, f'{file}')
            write_counts_to_file(counts, output_file)


        if len(files) != 0:
            count_all_wastes(output_folder_path)
