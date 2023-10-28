import os

# Ваш путь
path = 'путь_к_вашей_папке/последняя_папка'

# Получаем путь без последней папки
path_without_last_folder = os.path.dirname(path)

# Выводим результат
print(path_without_last_folder)