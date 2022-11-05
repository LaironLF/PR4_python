import time
from watchdog.observers import Observer
from shedule_class import FileSchedule


event_handler = FileSchedule('./files/log.txt')
observer = Observer()
observer.schedule(event_handler, './files', recursive=True)
observer.start()

try:
    while True:
        time.sleep(1)
finally:
    observer.stop()
    observer.join()
