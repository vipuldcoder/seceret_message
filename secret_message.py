import os
def rename_files():
    #(1) get file names from a folder
    file_list = os.listdir(r"C:\Users\Vipul\Pictures\prank\prank")
    print(file_list)
    save_path = os.getcwd()
    os.chdir(r"C:\Users\Vipul\Pictures\prank\prank")
    print(" Current work directory "+save_path)
    #(2) for each file, rename filename
    for file_name in file_list:
        os.rename(file_name, file_name.translate("0123456789"))
    os.chdir(save_path)    
rename_files()    
