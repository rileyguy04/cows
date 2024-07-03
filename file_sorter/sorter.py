import os
import shutil
from PIL import Image

##__## FUNCTIONS FOR SETUP ##__##
def ap(original_path, appended_str):
    # ap : AP : Append to Path
    return original_path + '//' + appended_str

def get_path():
    cur_directory = os.getcwd().split('\\')
    path = ""
    cur_directory.pop()
    for dir in cur_directory:
        path += dir + '\\'
    return path

def del_extra_folders(path):
    conds = ['DO NOT TOUCH','Post FLIR']
    for folder in os.listdir(path):
        if not any(cond in folder for cond in conds):
            shutil.rmtree(ap(path,folder))

def del_non_jpgs(path):
    files = os.listdir(path)
    for file in files:
        if file.find('.jpg') == -1 and file.find('.') != -1:
            os.remove(ap(path, file))

def del_extra_POST(path):
    conds = ['10_28', '11_11', '11_18', '12_1']
    path += '\\' + 'Post FLIR'
    tree_conts = os.listdir(path)
    for folder in tree_conts:
        if not any(cond in folder for cond in conds):
            if folder.find('.') == -1:
                shutil.rmtree(ap(path, folder))
            else:
                os.remove(ap(path, folder))

def recursive_copy(folder_path, output_path):
    contents = os.listdir(folder_path)
    print(folder_path)
    print(output_path)
    for content in contents:
            content_path = ap(folder_path, content)
            if os.path.isdir(content_path) and content.find('.zip') == -1:
                recursive_copy(content_path, output_path)
            elif content.find('.zip') == -1:
                if folder_path == 'C:\\Users\\riley\\Desktop\\Cows\\Editable Files\\FLIR IMAGES\\Post FLIR': #  Testing
                    shutil.move(content_path, output_path)
            else:
                print('Error, cannot handle: \n\t' + content_path)

##  END OF FUNCTIONS FOR SETUP   ##

################################################################################
################################################################################
################################################################################

def setup():
    mainPath = get_path() + 'cows\\Editable Files\\FLIR IMAGES'
    outPath = get_path() + 'cows\\file_sorter\\output_files'
    folders = os.listdir(mainPath)

    del_extra_folders(mainPath)
    del_extra_POST(mainPath)

    for folder in folders:
        del_non_jpgs(ap(mainPath, folder))

    if os.path.isdir(outPath):
        shutil.rmtree(outPath)
    os.makedirs(outPath)

    recursive_copy(mainPath, outPath)

################################################################################
################################################################################
################################################################################

setup()