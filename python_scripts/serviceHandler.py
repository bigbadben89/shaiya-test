import utils
import sys
import os
import time

sqlCmd = "python sqlHandler.py executeQuery \"%s\""
psGameExec = "EXEC OMG_GameWEB.dbo.command @serviceName = N'ps_game', @cmmd = N'%s'"
psLoginExec = "EXEC OMG_GameWEB.dbo.command @serviceName = N'ps_login', @cmmd = N'%s'"
cmd = ""
messageDelimeter = "|"

def inGameNotice(c):
    utils.show("Starting ingame auto notice...")
    while True:
        sql = utils.loadConfig(utils.dbFile)
        enabled = sql["ingame_notice.enabled"]
        if enabled.lower() == "false":
            utils.show("Ingame notice enabled = %s!!! You might want to change ingame_notice.enabled=true to start ingame notice." % enabled)
            break

        messages = sql["ingame_notice.messages"]
        for m in messages.split(messageDelimeter):
            utils.show("Sending \"%s\" to ps_game..." % m)
            utils.executeCommand(c % ("/nt " + m))
            time.sleep(15)

        interval = int(sql["ingame_notice.interval"])
        utils.show("Waiting for %d second(s) to notice \"%s\"" % (interval, messages))
        time.sleep(interval)

if __name__== "__main__":
    choice = sys.argv[1]
    if choice == "inGameNotice":
        cmd = sqlCmd % psGameExec
        inGameNotice(cmd)
    elif choice == "nprotectoff":
        psGameExec = psGameExec % "/nprotectoff"
        cmd = sqlCmd % psGameExec
        utils.executeCommand(cmd)
    elif choice == "vchkoff":
        psLoginExec = psLoginExec % "/vchkoff"
        cmd = sqlCmd % psLoginExec
        utils.executeCommand(cmd)
    elif choice == "vchkon":
        psLoginExec = psLoginExec % "/vchkon"
        cmd = sqlCmd % psLoginExec
        utils.executeCommand(cmd)



