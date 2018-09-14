import os
from datetime import datetime

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
    return datetime.now().strftime('%Y-%m-%d_%H:%M:%S')
