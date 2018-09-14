import os
from datetime import datetime

7zCompressCmd = r"C:\Program Files\7-Zip\7z.exe a %s %s"

def show(s):
    print "*** " + str(s).upper()

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
    compressedFile = os.path.join(parent, folderToCompress + ".7z")
    show("Compressing %s to %s" % (completePath, compressedFile))
    executeCommand(7zCompressCmd % (compressedFile, completePath))
    show("Compressing done!!! Removing folder %s" % folderToCompress)
    os.remove(completePath)

