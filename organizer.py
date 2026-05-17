import config
import os


def get_folder(ext):
    for folder in config.FILE_TYPES:
        if ext in config.FILE_TYPES[folder]:
            return folder
    return "others"

def organise(folder_path):
    try:
        file_entries=[f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path,f))]
    except FileNotFoundError:
        print("The specific folder doesn't exist.")
    except PermissionError:
        print("You don't have permission to access this directory.")
    except NotADirectoryError:
        print("The path provided points to a file, not a folder")
    else:
        for file in file_entries:
            file_path=os.path.join(folder_path,file)