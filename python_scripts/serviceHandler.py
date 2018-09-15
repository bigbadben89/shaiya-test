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
            utils.executeCommand(c + m)
            time.sleep(15)

        interval = int(sql["ingame_notice.interval"])
        utils.show("Waiting for %d second(s) to notice \"%s\"" % (interval, messages))
        time.sleep(interval)

def vchkoff(c):
    utils.show("Sending /vchkoff to ps_login...")
    utils.executeCommand(c)

def vchkon(c):
    utils.show("Sending /vchkon to ps_login...")
    utils.executeCommand(c)

def nprotectoff(c):
    utils.show("Sending /nprotectoff to ps_game...")
    utils.executeCommand(c)

if __name__== "__main__":
    choice = sys.argv[1]
    if choice == "inGameNotice":
        psGameExec = psGameExec % "/nt "
        cmd = sqlCmd % psGameExec
        inGameNotice(servuceCmd)
    else choice == "startService":
        psGameExec = psGameExec % "/nprotectoff"
        cmd = sqlCmd % psGameExec
        nprotectoff(serviceCmd)
        psLoginExec = psLoginExec % "/vchkoff"
        cmd = sqlCmd % psLoginExec
        vchkoff(serviceCmd)


