__author__ = 'A'

import watchdog as wd
import os
import subprocess
import time
import datetime

class Desktopeventhandler(wd.events.FileSystemEventHandler):

    def on_created(self, event):
        # list_of_files = os.listdir('/Users/second/Desktop')
        files = [file for file in os.listdir('/Users/second/Desktop') if os.path.isfile(os.path.join('/Users/second/Desktop', file))]
        ts = time.time()
        st = 'Data'+datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d-%H:%M:%S')
        if len(files) > 5:
            # subprocess.call(['mkdir', '/Users/second/Desktop/'+st])
            # commands.getstatusoutput('cd /Users/second/Desktop/')
            for file in files:
                subprocess.call(['mv', os.path.join('/Users/second/Desktop', file), '/Users/second/Desktop/Data/'])
