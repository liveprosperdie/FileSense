import config


def get_folder(ext):
    for folder in config.file_types:
        if ext in config.file_types[folder]:
            return folder
    return "others"

def organise(path):
    