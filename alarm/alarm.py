import subprocess
from threading import Timer
import webbrowser
import datetime

def startmusic():
    if datetime.datetime.now().time().minute >= 30 and datetime.datetime.now().time().hour >= 6:
        #subprocess.call(['/Applications/VLC.app/Contents/MacOS/VLC', '-I', 'rc', '/Users/second/Desktop/ZYBY.mp3'])
        webbrowser.open_new('https://www.youtube.com/watch?v=nPhHtahBlyI')
        Timer(600, startmusic, ()).start()
    else:
        Timer(5, startmusic, ()).start()


startmusic()