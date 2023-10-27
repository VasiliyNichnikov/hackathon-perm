import os

from our_solutions.paths import get_no_sorted_data_path, get_path_to_folder_for_transformed_data

array_name = ['video0', 'video1', 'video2']
for name_txt in array_name:
    with open(get_no_sorted_data_path(f'{name_txt}'), 'r') as file:
        lines = file.readlines()

    data_dict = {}
    for line in lines:
        elements = line.split()
        photo_num = elements[0]
        if photo_num not in data_dict:
            data_dict[photo_num] = []
        data_dict[photo_num].append(elements[2:])

    for photo_num, data in data_dict.items():
        file_name = f'{photo_num}.txt'
        file_name = file_name.replace(",", "")
        folder_path = get_path_to_folder_for_transformed_data(name_txt)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
        file_path = os.path.join(folder_path, file_name)
        with open(file_path, 'w') as file:
            for item in data:
                file.write(' '.join(item) + '\n')
