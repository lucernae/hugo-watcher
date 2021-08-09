import subprocess
import time
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler

if __name__ == "__main__":
    patterns = ["*"]
    ignore_patterns = None
    ignore_directories = False
    case_sensitive = True
    my_event_handler = PatternMatchingEventHandler(patterns, ignore_patterns, ignore_directories, case_sensitive)

def on_created(event):
    print(f"{event.src_path} has been created!")
    run_hugo()

def on_deleted(event):
    print(f"File / path deleted: {event.src_path}!")
    run_hugo()

def on_modified(event):
    print(f"{event.src_path} has been modified")
    run_hugo()

def on_moved(event):
    print(f"File moved {event.src_path} to {event.dest_path}")
    run_hugo()

def run_hugo():
    cp = subprocess.run(["/bin/hugo"])


my_event_handler.on_created = on_created
my_event_handler.on_deleted = on_deleted
my_event_handler.on_modified = on_modified
my_event_handler.on_moved = on_moved

path = "/src/content/"
go_recursively = True
my_observer = Observer()
my_observer.schedule(my_event_handler, path, recursive=go_recursively)

my_observer.start()
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    my_observer.stop()
    my_observer.join()
