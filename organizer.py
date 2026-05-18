import os
import config
import logger
import shutil


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
            _,extension=os.path.splitext(file_path)
            folder_name=get_folder(extension)
            target_folder_path=os.path.join(folder_path,folder_name)
            try:
                os.makedirs(target_folder_path, exist_ok=True)
                shutil.move(file_path,target_folder_path)
                logger.log_action(f"Successfully moved {file} to {folder_name} folder")
            except PermissionError:
                print("Error: You do not have permission to create a folder here.")
                logger.log_action("Error: You do not have permission to create a folder here.","error")
            except FileExistsError:
                print("Folder name already in use")
                logger.log_action("Folder name already in use","error")
            except shutil.Error:
                print (f"{file} can't be moved")
                logger.log_action(f"{file} can't be moved","error")
                