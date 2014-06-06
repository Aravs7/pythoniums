__author__ = 'A'
import os
import subprocess
print('file created')
home = os.getenv("HOME")
desktop = home + '/Desktop'
allfiles = os.listdir(desktop)
files = [file for file in allfiles if os.path.isfile(os.path.join(desktop, file))]
if 'auto_store' not in allfiles:
    subprocess.call(['mkdir', desktop+'/auto_store'])
if len(files) > 5:
    for file in files:
        subprocess.call(['mv', os.path.join(desktop, file), desktop+'/auto_store/'])
