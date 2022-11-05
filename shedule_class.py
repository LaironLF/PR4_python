from watchdog.events import FileSystemEventHandler
class FileSchedule(FileSystemEventHandler):

    def __init__(self, file_path) -> None:
        self._file_path = file_path
    
    def on_modified(self, event):
        # return super().on_modified(event)
        with open(self._file_path, 'r') as file:
            print(file.readlines()[-1])
        