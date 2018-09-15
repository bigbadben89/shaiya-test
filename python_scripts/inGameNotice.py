import utils
import os
import time

noticeConf = os.path.join("..", "config", "notice.conf")
sqlCmd = "python sqlHandler.py executeQuery \"%s\""
noticeExec = "EXEC OMG_GameWEB.dbo.command @serviceName = N'ps_game', @cmmd = N'/nt %s'"
fullNoticeCmd = sqlCmd % noticeExec
messageDelimeter = "|"

def main():
    utils.show("Starting ingame auto notice...")
    while True:
        sql = utils.loadConfig(noticeConf)
        enabled = sql["ingame_notice.enabled"]
        if enabled.lower() == "false":
            utils.show("Ingame notice enabled = %s" % enabled)
            continue

        messages = sql["ingame_notice.messages"]
        for m in messages.split(messageDelimeter):
            utils.show("Sending \"%s\" to ps_game..." % m)
            utils.executeCommand(fullNoticeCmd % m)
            time.sleep(15)

        interval = int(sql["ingame_notice.interval"])
        utils.show("Waiting for %d second(s) to notice \"%s\"" % (interval, messages))
        time.sleep(interval)

if __name__== "__main__":
    main()
