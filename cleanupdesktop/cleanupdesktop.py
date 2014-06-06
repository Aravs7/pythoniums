__author__ = 'A'

import time
import logging
from watchdog.observers import Observer
import watchdog.events as wde
import eventhandling
import os

if __name__ == "__main__":
    print("Starting listener ...")
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    event_handler = eventhandling.Desktopeventhandler()
    event_handler.cleanup()
    observer = Observer()
    observer.schedule(event_handler, os.getenv('HOME')+'/Desktop', recursive=True)
    observer.schedule(wde.LoggingEventHandler(), os.getenv('HOME')+'/Desktop', recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()