import shutil
import os

from_dir = "C:/Users/vinic/Downloads"
to_dir = "C:/Users/vinic/Arquivos_Documentos"

list_of_files = os.listdir(from_dir)
# print(list_of_files)

for file_name in list_of_files:
    name, extension = os.path.splitext(file_name)
    if extension == '':
        continue
    if extension in ['.txt', '.doc', '.docx', '.pdf']:
        path1 = from_dir + '/' + file_name
        path2 = to_dir
        path3 = to_dir + '/' + file_name
        if not os.path.exists(path2):
            os.makedirs(path2)
        print("Movendo "+file_name+"...")
        shutil.move(path1, path3)
