import utils 
import sys
import subprocess
import os

dbFile = os.path.join("..", "config", "db.conf")
dbBackUpPath = os.path.join("C:", "DATABASE_BACKUP")

sqlCommon = "sqlcmd -U %s -P %s -S %s"
sqlBackUpQuery = "BACKUP DATABASE %s TO DISK = \"%s\" GO"
sqlExecuteFile = ""
sqlExecuteQuery = ""

def executeSqlFile(sqlFile):
    if not utils.checkIfFileExisted(sqlFile):
        utils.show("Failed to execute %s" % sqlFile)
        return
    utils.executeCommand(sqlExecuteFile % sqlFile)   

def executeSqlQuery(query):
    utils.show("Executing %s" % query)
    utils.executeCommand(query)

if __name__== "__main__":
    operation = sys.argv[1]
    if not operation:
        utils.show("No operation has been given!!!")
        sys.exit()

    sqlConf = utils.loadConfi(dbFile)

    if sqlConf:
        sqlCommon = sqlCommon % (sqlConf["db.user"], sqlConf["db.pass"], sqlConf["db.host"])
        sqlExecuteFile = sqlCommon + " -i %s"
        sqlExecuteQuery = sqlCommon + " -Q %s"

    if operation == "executeFile":
        sqlFile = sys.argv[2]
        executeSqlFile(sqlFile)
    elif operation == "backup":
        currentTime = utils.getCurrentTime()
        newDbBackUpPath = os.path.join(dbBackUpPath, currentTime)
        utils.show("Creating  %s" % newDbBackUpPath)
        utils.createDirectory(newDbBackUpPath)
    
        backUpQuery = sqlExecuteQuery % sqlBackUpQuery
        executeSqlQuery(backUpQuery % ("OMG_GameWEB", os.path.joint(newDbBackUpPath, "OMG_GameWeb", currentTime)))
        executeSqlQuery(backUpQuery % ("PS_Billing", os.path.joint(newDbBackUpPath, "PS_Billing", currentTime)))
        executeSqlQuery(backUpQuery % ("PS_ChatLog", os.path.joint(newDbBackUpPath, "PS_ChatLog", currentTime)))
        executeSqlQuery(backUpQuery % ("PS_GameData", os.path.joint(newDbBackUpPath, "PS_GameData", currentTime)))
        executeSqlQuery(backUpQuery % ("PS_GameDefs", os.path.joint(newDbBackUpPath, "PS_GameDefs", currentTime)))
        executeSqlQuery(backUpQuery % ("PS_GameLog", os.path.joint(newDbBackUpPath, "PS_GameLog", currentTime)))
        executeSqlQuery(backUpQuery % ("PS_GMTool", os.path.joint(newDbBackUpPath, "PS_GMTool", currentTime)))
        executeSqlQuery(backUpQuery % ("PS_Statics", os.path.joint(newDbBackUpPath, "PS_Statics", currentTime)))
        executeSqlQuery(backUpQuery % ("PS_UserData", os.path.joint(newDbBackUpPath, "PS_Userdata", currentTime)))

        utils.compress(dbBackUpPath, currentTime)
    else:
        utils.show("Operation failed! We do not have %s operation" % operation)
