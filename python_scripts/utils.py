import os
import sys
from datetime import datetime

shaiyaConfigPath = os.path.join("C:", "ShaiyaServer", "PSM_Client", "Bin", "Config")
7zPath = os.path.join("C:", "Program Files", "7-Zip", "7z.exe")
7zCompressCmd = r+ "" + 7zPath + " a %s %s"

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
    completePath = os.path.joint(parent, folderToCompress)
    compressedFile = os.path.join(completePath + ".7z")
    show("Compressing %s to %s" % (completePath, compressedFile))
    executeCommand(7zCompressCmd % (compressedFile, completePath))
    show("Compressing done!!! Removing folder %s" % folderToCompress)
    os.remove(completePath)

def loadConfig(configFile):
    isFileExisted = checkIfFileExisted(configFile)
    if not isFileExisted:
        sys.exit()
        return

    config = {}
    with open(dbFile) as f:
        for line in f.readlines():
            l = line.strip().split("=")
            config[l[0]] = l[1]
    return config
