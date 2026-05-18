import time
import logger
import organizer
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class Folder_Handler(FileSystemEventHandler):
    
    def __init__(self,folder_path):
        self.folder_path=folder_path

    def on_created(self, event):
        if not event.is_directory:
            organizer.organise(self.folder_path)
            logger.log_action(f"{event.src_path} created")


def observe(folder_path):
    event_handler=Folder_Handler(folder_path)
    observer=Observer()
    observer.schedule(event_handler, path=folder_path, recursive=False)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()
    