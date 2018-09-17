import utils 
import sys
import subprocess
import os

dbBackUpPath = os.path.join("C:\\", "DATABASE_BACKUP")

sqlCommon = "sqlcmd -U %s -P %s -S %s"
sqlBackUpQuery = "BACKUP DATABASE %s TO DISK=\'%s\'"
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
    operation = sys.argv[1].lower()
    if not operation:
        utils.show("No operation has been given!!!")
        sys.exit()

    sqlConf = utils.loadConfig(utils.dbFile)

    if sqlConf:
        sqlCommon = sqlCommon % (sqlConf["db.user"], sqlConf["db.pass"], sqlConf["db.host"])
        sqlExecuteFile = sqlCommon + " -i \"%s\""
        sqlExecuteQuery = sqlCommon + " -Q \"%s\""

    if operation == "executefile":
        sqlFile = sys.argv[2]
        executeSqlFile(sqlFile)
    elif operation == "executequery":
        sqlQuery = sys.argv[2]
        executeSqlQuery(sqlExecuteQuery % sqlQuery)
    elif operation == "backup":
        currentTime = utils.getCurrentTime()
        newDbBackUpPath = os.path.join(dbBackUpPath, currentTime)
        utils.show("Creating  %s" % newDbBackUpPath)
        utils.createDirectory(newDbBackUpPath)
    
        backUpQuery = sqlExecuteQuery % sqlBackUpQuery
        executeSqlQuery(backUpQuery % ("OMG_GameWEB", os.path.join(newDbBackUpPath, "OMG_GameWeb.bak")))
        executeSqlQuery(backUpQuery % ("PS_Billing", os.path.join(newDbBackUpPath, "PS_Billing.bak")))
        executeSqlQuery(backUpQuery % ("PS_ChatLog", os.path.join(newDbBackUpPath, "PS_ChatLog.bak")))
        executeSqlQuery(backUpQuery % ("PS_GameData", os.path.join(newDbBackUpPath, "PS_GameData.bak")))
        executeSqlQuery(backUpQuery % ("PS_GameDefs", os.path.join(newDbBackUpPath, "PS_GameDefs.bak")))
        executeSqlQuery(backUpQuery % ("PS_GameLog", os.path.join(newDbBackUpPath, "PS_GameLog.bak")))
        executeSqlQuery(backUpQuery % ("PS_GMTool", os.path.join(newDbBackUpPath, "PS_GMTool.bak")))
        executeSqlQuery(backUpQuery % ("PS_Statics", os.path.join(newDbBackUpPath, "PS_Statics.bak")))
        executeSqlQuery(backUpQuery % ("PS_UserData", os.path.join(newDbBackUpPath, "PS_UserData.bak")))

        utils.compress(dbBackUpPath, currentTime)
    else:
        utils.show("Operation failed! We do not have %s operation" % operation)
