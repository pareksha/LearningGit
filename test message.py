import os

def file_rename():
    current_path = os.getcwd()
    os.chdir(r"C:\Users\Pareksha\Desktop\test")
    file_list = os.listdir(r"C:\Users\Pareksha\Desktop\test")
    for file_name in file_list:
        os.rename(file_name, file_name.translate(None,"0123456789"))
    os.chdir(current_path)

file_rename()
