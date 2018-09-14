import utils
import os

noticeConf = os.path.join("..", "config", "notice.conf")
sqlCmd = "python sqlHandler.py executeQuery %s"
noticeExec = "EXEC OMG_GameWEB.dbo.command @serviceName = N'ps_game', @cmmd = N'/nt %s'"

def main():
    while True:
        sql = utils.loadConfig(noticeConf)
        enabled = sql["ingame_notice.enabled"]
        interval = sql["ingame_notice.interval"]
        time.sleep(interval)
        if lower(enabled) == "false":
            utils.show("Ingame notice enabled = %s" % enabled)
            continue
        message = sql["ingame_notice.message"]
        utils.show("Sending \"%s\" to ps_game..." % message)
        utils.executeCommand(sqlCmd % noticeExec)

if __name__== "__main__":
    main()
