import os
import logging


def log_action(message,log_type="info"):
    folder_path=os.path.join(os.path.dirname(__file__),"logs")
    os.makedirs(folder_path, exist_ok=True)
    file_path=os.path.join(folder_path,"File_action.log")
    logging.basicConfig(
        filename=file_path,
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S")
    if log_type=="info":
        logging.info(message)
    elif log_type=="error":
        logging.error(message)