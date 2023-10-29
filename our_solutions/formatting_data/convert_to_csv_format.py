import os
import csv

from our_solutions.paths import get_path_to_csv, get_path_to_save_txt, get_path_to_all_save_txt

with open(os.path.join(get_path_to_save_txt(), 'output.csv'), 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(['frame_id;wood;glass;plastic;metal'])
    for root, dirs, files in os.walk(get_path_to_csv()):
        for index_file, file in enumerate(files):
            name_frame = int(file.replace('.txt', ''))
            file_path = os.path.join(root, file)
            array_string = f'f{name_frame}'

            with open(file_path, 'r') as f:
                lines = f.readlines()
                for id_line, line in enumerate(lines):
                    if id_line in range(0, 4):
                        new_string = ';' + line
                        array_string += new_string
            array_string = array_string.replace('\n', '')
            csv_writer.writerow([array_string])
    array_string = 'f_all'
    with open(get_path_to_all_save_txt(), 'r') as f:
        lines = f.readlines()
        for id_line, line in enumerate(lines):
            if id_line in range(0, 4):
                array_string += ';' + line
    array_string = array_string.replace('\n', '')
    csv_writer.writerow([array_string])