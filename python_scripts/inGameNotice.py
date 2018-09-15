import utils
import os
import time

noticeConf = os.path.join("..", "config", "notice.conf")
sqlCmd = "python sqlHandler.py executeQuery \"%s\""
noticeExec = "EXEC OMG_GameWEB.dbo.command @serviceName = N'ps_game', @cmmd = N'/nt %s'"
<<<<<<< HEAD
messageDelimeter = "|"
=======
fullNoticeCmd = sqlCmd % noticeExec
>>>>>>> 0b6c0813729d57dbe3669dd5b1ed35ef81d333b3

def main():
    utils.show("Starting ingame auto notice...")
    while True:
        sql = utils.loadConfig(noticeConf)
        enabled = sql["ingame_notice.enabled"]
        if enabled.lower() == "false":
            utils.show("Ingame notice enabled = %s" % enabled)
            continue
<<<<<<< HEAD
        messages = sql["ingame_notice.messages"]
        for m in messages.split(messageDelimeter):
            utils.show("Sending \"%s\" to ps_game..." % message)
            utils.executeCommand(sqlCmd % noticeExec)
            time.sleep(15)
=======
        
        interval = int(sql["ingame_notice.interval"])
        message = sql["ingame_notice.message"]
        utils.show("Waiting for %d second(s) to notice \"%s\"" % (interval, message))
        time.sleep(interval)
        utils.show("Sending \"%s\" to ps_game..." % message)
        utils.executeCommand(fullNoticeCmd % message)
>>>>>>> 0b6c0813729d57dbe3669dd5b1ed35ef81d333b3

if __name__== "__main__":
    main()
