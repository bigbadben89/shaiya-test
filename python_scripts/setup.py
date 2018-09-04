import socket

psGameFile = "C:\\ShaiyaServer\\PSM_Client\\Bin\\Config\\ps_game.ini"
psSessionFile = "C:\\ShaiyaServer\\PSM_Client\\Bin\\Config\\ps_session.ini"

def replaceInFile(filename, fromText, toText):
    if toText == "":
        toText = "Shaiya SGolden"
    f = open(filename, "r")
    lines = f.readlines()
    f.close()
    for i, line in enumerate(lines):
        s = line.split("=")
        if s[0] == fromText:
            lines[i] = fromText + "=" + toText + "\r\n"
    f = open(filename, "w")
    f.write("".join(lines))
    f.close()

def main():
    serverName = raw_input("Enter your server name: ")
    replaceInFile(psGameFile, "GameName", serverName)
    replaceInFile(psSessionFile, "Game01", serverName)

    publicIp = raw_input("Enter your ip: ")
    
    #s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    #s.connect(('8.8.8.8', 53))
    #localIP = s.getsockname()[0]
    #print "Your IP address:", localIP
    replaceInFile(psGameFile, "GamePublicIP", publicIp)

    print "########################################"
    print ""
    print "*** DEFAULT SERVER NAME: Shaiya SGolden"
    print ""
    print "*** YOU HAVE CHANGED SERVER NAME TO " + serverName
    print ""
    print "*** YOUR GAME SERVER IP " + publicIp
    print "########################################"

if __name__== "__main__":
    main()