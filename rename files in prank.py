import os
def rename_files():
    file_list = os.listdir(r"C:\Users\Pareksha\Downloads\prank")
    print(file_list)
    current_path = os.getcwd()
    print "Current working directory is", current_path
    os.chdir(r"C:\Users\Pareksha\Downloads\prank")
    for file_name in file_list:
        os.rename(file_name, file_name.translate(None,"0123456789"))
    os.chdir(current_path)

rename_files()
