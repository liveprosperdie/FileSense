import config


def get_folder(ext):
    for folder in config.FILE_TYPES:
        if ext in config.FILE_TYPES[folder]:
            return folder
    return "others"

def organise(path):
    