import socket
import os 
import utils

psGameFile = os.path.join(utils.shaiyaConfigPath, "ps_game.ini")
psSessionFile = os.path.join(utils.shaiyaConfigPath, "ps_session.ini")

defaultServerName = "Shaiya SGolden"

def replaceInFile(filename, fromText, toText):
    if toText == "":
        toText = defaultServerName
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
    print "*** DEFAULT SERVER NAME: " + defaultServerName
    print ""
    print "*** YOU HAVE CHANGED SERVER NAME TO " + serverName
    print ""
    print "*** YOUR GAME SERVER IP " + publicIp
    print ""
    print "########################################"

if __name__== "__main__":
    main()
