


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
