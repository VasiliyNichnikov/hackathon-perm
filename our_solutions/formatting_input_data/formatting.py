import os

from our_solutions.paths import get_no_sorted_data_path

array_name = ['video0', 'video1', 'video1']
for name_txt in array_name:
    with open(get_no_sorted_data_path(f'{name_txt}'), 'r') as file:
        lines = file.readlines()

    output_folder = f'../transformed_data/{name_txt}/'

    data_dict = {}
    for line in lines:
        elements = line.split()
        photo_num = elements[0]
        if photo_num not in data_dict:
            data_dict[photo_num] = []
        data_dict[photo_num].append(elements[2:])

    # Запись данных в отдельные файлы в указанной папке
    for photo_num, data in data_dict.items():
        file_name = f'{photo_num}.txt'
        file_name = file_name.replace(",", "")  # Удаление запятой из имени файла
        file_path = os.path.join(output_folder, file_name)
        with open(file_path, 'w') as file:
            for item in data:
                file.write(' '.join(item) + '\n')
