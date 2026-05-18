import organizer
import logger
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class Folder_Handler(FileSystemEventHandler):
    
    def __init__(self,folder_path):
        self.folder_path=folder_path

    def on_created(self, event):
        if not event.is_directory:
            organizer.organise(self.folder_path)


