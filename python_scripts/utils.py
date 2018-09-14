import os
import shutil
import sys
import subprocess
from datetime import datetime

dbFile = os.path.join("..", "config", "db.conf")
shaiyaConfigPath = os.path.join("C:\\", "ShaiyaServer", "PSM_Client", "Bin", "Config")
_7zPath = os.path.join("C:\\", "Program Files", "7-Zip", "7z.exe")
_7zCompressCmd = r"" + _7zPath + " a %s %s"

def show(s):
    print "*** " + str(s).upper()

def createDirectory(p):
    os.makedirs(p)

def checkIfFileExisted(f):
    existed = os.path.isfile(f)
    if existed:
        show("Reading %s" % f)
    else:
        show("%s does not exist!!!" % f)
    return existed

def getCurrentTime():
    return datetime.now().strftime('%Y-%m-%d_%H-%M-%S')

def executeCommand(c):
    subprocess.call(c, shell=False)

def compress(parent, folderToCompress):
    completePath = os.path.join(parent, folderToCompress)
    compressedFile = completePath + ".7z"
    show("Compressing %s to %s" % (completePath, compressedFile))
    executeCommand(_7zCompressCmd % (compressedFile, completePath))
    show("Compressing done!!! Removing folder %s" % folderToCompress)
    shutil.rmtree(completePath)

def loadConfig(configFile):
    isFileExisted = checkIfFileExisted(configFile)
    if not isFileExisted:
        sys.exit()
        return

    config = {}
    with open(configFile) as f:
        for line in f.readlines():
            l = line.strip().split("=")
            config[l[0]] = l[1]
    return config
